---
name: transaction-management-without
layout: post
title: Transaction Management without the Frameworks
time: 2012-01-29 13:58:00 +00:00
categories: java object-oriented
comments: true
sidebar : false
description: "Avoid frameworks like Spring and roll your own transaction management. Declarative approaches like Spring, by definition, take away control. Moving towards an imperative approach gives it back. Don't be put of, it's actually very straight forward."
keywords: "transactions, acid, transaction management, transactionality, GOOS, unit of work, declarative vs imperative, spring"
---

It's easy to avoid manually managing transactions when frameworks like Spring and containers do a good job of hiding all the details. However, it's often more advantageous to take the controls and manage your own transactions. We seem to shy away from this but its really straight forward and if it means we're not tied into yet another framework, why wouldn't we? Aside from just avoiding frameworks though, how does replacing `@Transctional` with something bespoke really help us?
  
Moving from a declarative approach to a more imperative one can help us with testing and by virtue; _composability_. We can move from something which can only be tested using the framework or container (implying an integration or end-to-end style test) to a more focused style (without the need of said frameworks or containers). If we manage things ourselves and are explicit about the transactional boundaries in production code, we can be more lightweight in our tests.

<!-- more -->

Lets take a look at an example in detail.

It's probably helpful to be clear what we mean by a _unit of work_ here. Intimately related to the idea of a database transaction, a unit of work is a series of database operations that when applied together adhere to all the transactional characteristics (_atomic_, _coherent_, _isolated_ and _durable_). For example, when updating the database to increment one bank account and decrementing another, things should be atomic (both operations happen or neither does), consistent (the bank accounts actually exist), isolated (protected from concurrent updates to the same accounts) and durable (permanently applied). Describing both operations as a unit of work and applying then transactionally achieves this.

So we can think of the unit of work as something that can be executed and when it is, it'll be under the conditions described above.

  

``` java
public interface UnitOfWork<R, E extends Exception> {
    R execute(SessionProvider sessionProvider) throws E;
}
```
  
Something that would be responsible for executing the unit of work might look like this.

  

``` java
public interface UnitOfWorkRunner {
    <T, E extends Exception> T run(UnitOfWork<T, E> unitOfWork) throws Throwable;
}
```
  
When it comes to using Hibernate, we might have a concrete `UnitOfWorkRunner` look something like the following. The key thing here is that the transaction management is handled here, its a simple try catch finally pattern and as you can see, is very simple.


``` java
public class TransactionalUnitOfWorkRunner implements UnitOfWorkRunner {

    private final SessionProvider sessionProvider;

    public TransactionalUnitOfWorkRunner(SessionProvider sessionProvider) {
        this.sessionProvider = sessionProvider;
    }

    @Override
    public <T, E extends Exception> T run(UnitOfWork<T, E> unitOfWork) throws Throwable {
        Session session = sessionProvider.getCurrentSession();
        Transaction transaction = session.beginTransaction();
        try {
            T result = unitOfWork.execute(sessionProvider);
            transaction.commit();
            return result;
        } catch (Throwable e) {
            transaction.rollback();
            throw e;
        } finally {
            if (session.isOpen())
                session.close();
        }
    }

    public static <T, E extends Exception> T runInTransaction(SessionProvider sessionProvider, UnitOfWork<T, E> unitOfWork) throws Throwable {
        return new TransactionalUnitOfWorkRunner(sessionProvider).run(unitOfWork);
    }
}
```    

  
It's this class and interface that allows us to be explicit about our transactional boundary. Clients to this define the transaction boundary. In most containers and frameworks, the transactional boundary is around the request/response cycle and the developer has little influence. Using the `UnitOfWorkRunner` directly in your code gives more control over this. You can use a servlet filter to achieve a similar request/response scoped transaction or you can be finer grained and produce what I prefer; a transaction scoped to a coherent _business operation_.

  
For example, lets have a interface describing current account business functions that work on bank account entities. The `CurrentAccount` interface represents business functions and should define the transactional boundary. The `BankAccount` on the other hand represents the entities involved which themselves are stored in an `Accounts` _repostiory_.

  

    
``` java
// "business" operations
public interface CurrentAccount {
   void deposit(From<BankAccount> from, To<BankAccount> to);
}
```    

  
When we implement the `CurrentAccount`, we can define the transactional behavior as a separate concern from the business behavior. For example,

  

    
``` java
Accounts repository = new AccountRepository();
CurrentAccount currentAccount = new AcmeBankCurrentAccount(repository);
CurrentAccount transactionally = transactionally(sessionProvider, currentAccount);
// ...
transactionally.deposit(...);
```    

  
Where `transactionally` is a statically imported creation method that wires up the `AcmeBankCurrentAccount` (the business services) with transactional behavior. It does this via decoration but essentially creates an anonymous `UnitOfWork` in which to execute the business operation within.

  
The full class looks like this

  

    
``` java
public class TransactionWrapper<R> implements InvocationHandler {

    private final SessionProvider sessionProvider;
    private final R delegate;

    public static <R> R transactionally(SessionProvider sessionProvider, R object) {
        return (R) Proxy.newProxyInstance(object.getClass().getClassLoader(), object.getClass().getInterfaces(), new TransactionWrapper(sessionProvider, object));
    }

    public TransactionWrapper(SessionProvider sessionProvider, R delegate) {
        this.sessionProvider = sessionProvider;
        this.delegate = delegate;
    }

    @Override
    public Object invoke(Object proxy, final Method method, final Object[] args) throws Throwable {
        try {
            return new TransactionalUnitOfWorkRunner(sessionProvider).run(new UnitOfWork<Object, Exception>() {
                @Override
                public Object execute(SessionProvider sessionProvider) throws Exception {
                    return method.invoke(delegate, args);
                }
            });
        } catch (InvocationTargetException throwable) {
            throw throwable.getTargetException();
        }
    }
}
```    

  
The underlying business functionality within the `AcmeBankCurrentAccount` isn't concerned with transactions. Instead, its decorated with transactionality and we can use this decorating proxy to wrap any business interface as a transaction.

  

    
``` java
public class AcmeBankCurrentAccount implements CurrentAccount {

    private final AccountRepository accounts;

    public AcmeBankCurrentAccount(AccountRepository accounts) {
        this.accounts = accounts;
    }

    @Override
    public void deposit(From<BankAccountIdentifier> from, To<BankAccountIdentifier> to, Amount amount) throws Throwable {
        BankAccount benefactor =  accounts.find(from.value());
        BankAccount beneficiary = accounts.find(to.value());
        benefactor.withdraw(amount);
        beneficiary.deposit(amount);
        accounts.save(benefactor);
        accounts.save(beneficiary);
    }
}
```

This can come in handy when testing as we can isolate and test the different responsibilities. We're also left with a handy framework to add ad-hoc data directly to the database and it's easy enough to wire up an in-memory only `UnitOfWorkRunner`. Back to the point earlier about composability, the overall approach leaves us with loosely composed objects which combine to provide high level behavior. The composites are simpler than the sum of its parts to borrow a phrase from [GOOS](http://www.growing-object-oriented-software.com/).