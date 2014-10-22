---
layout: post
title: "Scala Mixins: The Right Way"
date: 2014-09-22 06:09
comments: true
categories: scala
sidebar: false
published: false
keywords: "scala, trait, mixin, ruby"
description: "Avoid the inheritance vs. composition argument by using mixin traits in the right way. Using inheritance to mixin behaviour contradicts the inheritance vs. composition principle, so when is a trait with behaviour a genuine mixin? Find out in this post."
---

Scala traits are interesting because they can be used for [inclusion polymorphism](http://en.wikipedia.org/wiki/Polymorphism_(computer_science)) **and** to [mixin](http://en.wikipedia.org/wiki/Mixin) behaviour. I've found tension here as the former uses inheritance and the later is more about code re-use. So when a Scala class extends a trait with behaviour, it seems to go against the generally accepted view that using inheritance as a mechanism for [code re-use is bad idea](http://baddotrobot.com/blog/2009/01/24/inheritance-vs-composition/). 

It can be tricky not break the [Inheritance vs. Composition](http://en.wikipedia.org/wiki/Composition_over_inheritance#Benefits) principle when using traits with behaviour.

<!-- more -->

## Mixins the Wrong Way

Odersky calls traits with behaviour "mixin traits". To be a genuine mixin trait, it should be used to mixin behaviour and not just something you inherit. But what's the difference? Let's look at an example using a test fixture trait.

Let's say that you have a [repository](http://martinfowler.com/eaaCatalog/repository.html) style class who's API talks about business operations, a `Customers` class for example. You might have an database backed version and you don't want anything going behind your back and messing with the data; everything in production code should go through your business API.

{% codeblock lang:scala %}
class OracleCustomers {
    def add(customer: Customer) = { ... }
    def getCustomer(id: CustomerId) = { ... }
    def getBasketValue(query: CustomerQuery) = { ... }
    def ship(query: CustomerQuery) = { ... }
}

{% endcodeblock %}

Now let's say that you want a test fixture to allow you to quickly setup test data in your `Customers` without having to go through the production API. You can provide an implementation to a trait and collect some data together like this;


{% codeblock lang:scala %}
trait BackdoorCustomers {       // <- base name, this is really a "fixture"
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
{% endcodeblock %}


This says that extending classes must provide a value for `customers`. It implements some coarse grained test setup against this. So when writing a test, it's easy to just extend the trait and slot in an implementation of `customers`. For example an `InMemoryCustomers` or an Oracle implementation that by-passes any constraint checking the proper API might enforce. 
 
 
{% codeblock lang:scala %}
class OracleCustomerTest extends BackdoorCustomers {        
    
    override val customers = new InMemoryCustomers
    
    application = ApplicationBuilder.with(customers)
    
    test("ensure basket totals are correct when discounts are applied") {
        this.addSomeCustomersWithFullBaskets()
        val result = application.doSomethingAgainstCustomersViaTheApi
        result should be (asExpected)
    }
}
{% endcodeblock %}

    
    
But we're saying here that an `OracleCustomerTest` **is a** `BackdoorCustomers`. That doesn't even make sense. There's no strong notion of a `BackdoorCustomers` in terms of a noun. What is one? Best case scenario, you're upfront about the fact that it's a fixture and rename `BackdoorCustomers` to `CustomersTestFixture` but even then, the *test* is not a *fixture*, the two are independent. One is test apparatus that supports the test, the other is the test or experiment itself.
 
It's tempting to use traits like this under the pretense of "mixing in" behaviour but you're really inheriting behaviour from something (that in our case) isn't related. You're precluding any type of substitution or inclusion polymorphism. Now arguably, substitution isn't of great value in test code like this but it's still a laudable goal.


## Proper Mixins
    
Using inheritance to mixin behaviour contradicts the inheritance vs. composition principle, so when is a trait with behaviour a genuine mixin? The trick is in _how_ we mix it in. Before, we made the **types** inherit the trait but we could have mixed it in for a specific **instance**.

For example, we can rework our trait to be a self type. 

{% codeblock lang:scala %}
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
{% endcodeblock %}

    
It now enforces implementers to also be a sub-type of `Customers`. This in turn forces us to rewrite the test

{% codeblock lang:scala %}
class OracleCustomerTest {        
    
    val customers = new InMemoryCustomers with BackdoorCustomers
    
    application = ApplicationBuilder.with(customers)
    
    test("ensure basket totals are correct when discounts are applied") {
        // ...
    }
}
{% endcodeblock %}

    

So now our test is not inheriting an orthogonal type. From an object-oriented perspective, it's much cleaner. We use composition to give the test (and application under test) the `customers` instance but this time, we treat it as two things. The actual type of the thing is
  
{% codeblock lang:scala %}
InMemoryCustomers with BackdoorCustomers
{% endcodeblock %}


So all the backdoor methods work along with the API methods but now we can clearer about which is which. For example,


{% codeblock lang:scala %}
customers.addSomeCustomersWithFullBaskets()         // <- a backdoor "fixture" method
application.doSomethingAgainstCustomersViaTheApi    // <- more likely to be a method under test

{% endcodeblock %}
    
    
    