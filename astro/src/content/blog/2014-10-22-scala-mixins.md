---
title: "Scala Mixins: The Right Way"
pubDate: '2014-09-22'
categories: 'scala'
keywords: "Scala traits, mixin, inheritance, composition, code reuse, Scala, ad-hoc polymorphism"
description: "Scala traits can be used for both polymorphism and mixins, but mixing these uses leads to trouble. Learn when using a trait as a mixin is genuinely appropriate."
heroImage: "/images/heroes/functional-programming.jpg"
---

Scala traits are interesting because they can be used for [inclusion polymorphism](http://en.wikipedia.org/wiki/Polymorphism_(computer_science) _and_ to [mixin](http://en.wikipedia.org/wiki/Mixin) behaviour. I've found tension here though, as the former uses inheritance and the later is more about code re-use. So when a Scala class extends a trait with behaviour, it seems to go against the generally accepted view that using inheritance as a mechanism for code re-use [is a bad idea](/blog/2009-01-24-inheritance-vs-composition/).

It can be tricky not break the [inheritance vs. composition](http://en.wikipedia.org/wiki/Composition_over_inheritance#Benefits) principle when using traits with behaviour. Is it clear to you when you might be?


## Mixins the Wrong Way

[Odersky](https://www.amazon.co.uk/Programming-Scala-Martin-Odersky/dp/0981531644/ref=as_sl_pc_ss_til?tag=baddotrobotco-21&linkCode=w01&linkId=DNXSQPP4AVLACD7U&creativeASIN=0981531644) calls traits with behaviour "mixin traits". To be a genuine mixin trait, it should be used to mixin behaviour and not just something you inherit from. But what's the difference? Let's look at an example.

Let's say that you have a [repository](http://martinfowler.com/eaaCatalog/repository.html) style class who's API talks about business operations, a `Customers` class for example. You might have an database backed version and you don't want anything going behind your back and messing with the data; everything in production code should go through your business API.

``` scala
class OracleCustomers {
    def add(customer: Customer) = { ... }
    def getCustomer(id: CustomerId) = { ... }
    def getBasketValue(query: CustomerQuery) = { ... }
    def ship(query: CustomerQuery) = { ... }
}
```
Now let's say that you want a test fixture to allow you to quickly setup test data in your `Customers` without having to go through the production API. You can provide an implementation to a trait and collect some data together like this;


``` scala
trait BackdoorCustomers {                               // <- bad name, this is really a "fixture"
    abstract val customers: Customers

    def addSomeCustomersWithFullBaskets() = {
        customers.add(RandomCustomer().with(RandomFullBasket()))
        customers.add(RandomDiscountedCustomer().with(RandomFullBasket()))            
    }

    def addSomeCustomersWithEmptyBaskets() = {
        customers.add(RandomCustomer())
        customers.add(RandomExpiredCustomer())
    }
}
```

This says that extending classes must provide a value for `customers`. It implements some coarse grained test setup against `customers`. So when writing a test, it's easy to just extend the trait and slot in an implementation of `customers`. For example an `InMemoryCustomers` or an Oracle implementation that by-passes any constraint checking the proper API might enforce.
 
 
``` scala
class OracleCustomerTest extends BackdoorCustomers {        
    
    override val customers = new InMemoryCustomers
    
    application = ApplicationBuilder.with(customers)
    
    test("ensure basket totals are correct when discounts are applied") {
        this.addSomeCustomersWithFullBaskets()
        val result = application.doSomethingAgainstCustomersViaTheApi
        result should be(asExpected)
    }
}
```
    
    
But we're saying here that an `OracleCustomerTest` _is a_ `BackdoorCustomers`. That doesn't even make sense. There's no strong notion of a `BackdoorCustomers`; it's not a meaningful _noun_. Best case scenario, you're upfront about the fact that it's a fixture and rename `BackdoorCustomers` to `CustomersTestFixture` but even then, the *test* is not a *fixture*, the two are independent. **One is test apparatus that supports the test, the other is the test or experiment itself**.
 
It's tempting to use traits like this under the pretense of "mixing in" behaviour but you're really inheriting behaviour from something (that in our case) isn't related. You're precluding any type of substitution or inclusion polymorphism. Now arguably, substitution isn't of great value in test code like this but it's still a laudable goal.


## Proper Mixins
    
Using inheritance to mixin behaviour contradicts the inheritance vs. composition principle. So just when is a trait with behaviour a genuine mixin? The trick is in _how_ we mix it in. Before, we made the _types_ inherit the trait but we could have mixed the trait into a specific _instance_.

For example, we can rework our trait to be a self type. 

``` scala
trait BackdoorCustomers {
    this: Customers =>
    
    def addSomeCustomersWithFullBaskets() = {
        add(RandomCustomer().with(RandomFullBasket()))
        add(RandomDiscountedCustomer().with(RandomFullBasket()))            
    }
    def addSomeCustomersWithEmptyBaskets() = {
        add(RandomCustomer())
        add(RandomExpiredCustomer())
    }
}
```
    
It now enforces implementers to also be a sub-type of `Customers`. This, in turn, forces us to rewrite the test

``` scala
class OracleCustomerTest {        
    
    private val customers = new InMemoryCustomers with BackdoorCustomers
    
    private val application = new ApplicationBuilder.with(customers)
    
    test("ensure basket totals are correct when discounts are applied") {
        // ...
    }
}
```
    

So now our test is not inheriting an orthogonal type. From an object-oriented perspective, it's much cleaner. We use composition to give the test a `customers` instance but this time, we treat it as two things. The actual type of the thing is;
  
``` scala
InMemoryCustomers with BackdoorCustomers
```

So all the backdoor methods work along with the API methods but now we can clearer about which is which. For example,


``` scala
customers.addSomeCustomersWithFullBaskets()         // <- a backdoor "fixture" method
application.doSomethingAgainstCustomersViaTheApi    // <- more likely to be the method under test
```    
## Conclusion

Scala is both an object-oriented language and a functional language. So unless your team is entirely behind doing things functionally, you're still going to come across object-oriented thinking and principles. Traits that have behaviour make it awkward because functionally-thinking, you could argue that nouns aren't important and behaviour in traits is just behaviour. So why not extend that behaviour by whatever means (including inheritance)?

Because Scala _has objects_ you can't really just ignore object-oriented semantics and thinking. Not unless, like I say, the entire team buy into functional only code. If that were the case, then reusable behaviour should really be represented as functions on [Scala singleton objects](http://tutorials.jenkov.com/scala/singleton-and-companion-objects.html) and not traits. You'd be forced to use composition anyway.

By that logic, it feels like extending traits for re-use in a functional programming context is just lazy. Mixing behaviour "the right way" seems much less contentious.


## Recommended Reading

* <a href="http://leanpub.com/whatsnewjava8">What's New in Java 8</a> (LeanPub), Toby Weston
* <a href="https://amzn.eu/d/f0iH92N">Learning Java Lambdas</a> (Amazon), Toby Weston
* <a href="https://amzn.eu/d/dcJRJ41">Learn Scala for Java Developers</a> (Amazon), Toby Weston

&nbsp;
&nbsp;
&nbsp;