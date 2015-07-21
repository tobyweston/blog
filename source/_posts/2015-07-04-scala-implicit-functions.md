---
layout: post
title: "Implicit Functions in Scala"
date: 2015-07-04 18:42
comments: true
categories: scala
sidebar: false
published: false
series: Scala Implicits
keywords: ""
description: ""
---

In the [previous post]({{ root_url }}/blog/2015/07/03/scala-implicit-parameters/), we looked at implicit parameters; parameters that will be automatically passed values annotated as `implicit`. In this post, we'll take a look at implicit functions and how they can be useful to convert things of one type to things of another.

<!-- more -->

## Implicit Functions

Implicit functions will be called automatically if the compiler thinks it's a good idea to do so. What that really means is that if your code doesn't compile but would if a call was made to an implicit function, Scala will call that function to make it compile. They're typically used to create _implicit conversion functions_; single argument functions to automatically convert from one type to another.

For example, the following function allows you to convert a Scala function into a instance of the Java 8 `Consumer` [single argument method]({{ root_url }}/blog/2014/04/07/functional-interfaces-in-java8/). 

{% codeblock lang:scala %}
implicit def toConsumer[A](function: A => Unit): Consumer[A] = new Consumer[A]() {
  override def accept(arg: A): Unit = function.apply(arg)
}
{% endcodeblock %}

We can use it to avoid having to write clunky anonymous class instantiation in Scala when interfacing with Java to mimic Java's lambda syntax. So rather than having to use the longhand version like this. 

{% codeblock lang:scala %}
def exampleUsingJavaForEach() {
  javaCollection.forEach(new Consumer[Element]() {
    override def accept(element: Element): Unit = ???
  })
}
{% endcodeblock %}

You can write this, where we just pass a Scala function to Java's `forEach` method.
 
{% codeblock lang:scala %}
def exampleUsingImplicitConversion() {
  javaCollection.forEach((element: Element) => ???)
}
{% endcodeblock %}

The argument to `forEach` is actually a function of type `Element => Unit`. Scala recognises that the `toConsumer` method could convert this into a `Consumer[Element]` and does so implicitly.     

{% codeblock lang:scala %}
def exampleUsingImplicitConversion() {
  val function: ObserverS => Unit = (observer) => observer.update(this, status)
  javaCollection.forEach(function)
}
{% endcodeblock %}

Which is basically short-hand for this.

{% codeblock lang:scala %}
def exampleUsingImplicitConversion() {
  val function: ObserverS => Unit = (observer) => observer.update(this, status)
  javaCollection.forEach(toConsumer(function))
}
{% endcodeblock %}

  
## Another Example

If we have a button on we web page that we'd like to find using [Web Driver](http://www.seleniumhq.org/projects/webdriver/), we'd normally write something like the following, using a "locator" to locate it by `id` attribute.

{% codeblock lang:scala %}
  val button: WebElement = driver.findElement(By.id("save-button")
  button.click()
{% endcodeblock %}

It doesn't take into account that the element might not be there when we call it (for example, when our UI uses ajax and adds the button asynchronously) and it's also a bit verbose. We can use an implicit function to address both of these issues.

The fragment below uses the [`WebDriverWait`](https://selenium.googlecode.com/git/docs/api/java/index.html?org/openqa/selenium/support/ui/WebDriverWait.html) class to wait for a UI element to appear on the screen (using `findElement` to check and retrying if necessary) and so smooths out the asynchronous issues.

{% codeblock lang:scala %}
implicit def waitForElement(locator: By): WebElement = {
  val predicate: WebDriver => WebElement = _.findElement(locator)
  new WebDriverWait(driver, 30).withMessage(s"waiting for element '$locator' on page '${driver.getCurrentUrl}'").until(predicate)
}
{% endcodeblock %}


It's also an implicit function designed to convert a `By` locator into a `WebElement`. It means we can write something like the following. Now `button` isn't a `WebElement` anymore but a `By`.

{% codeblock lang:scala %}
  val button = By.id("save-button")
  button.click()
{% endcodeblock %}  

Without the implicit `waitForElement` function, the code wouldn't compile; `By` doesn't have a `click` method on it. With the implicit function in scope however, the compiler works out that calling it (and passing in `create` as the argument), would return something that _does_ have the `click` method and would compile. 

## Single Arguments Only Please

Now there's one little bit I've brushed over here; how the `WebDriver` `driver` instance is available. The example above just assumes it's available but it'd be nicer to pass it into the function along with `locator`. However, there's a restriction of passing only a single argument into an implicit function. The answer is to use a second argument (using Scala's built in currying support). By combining implicit parameters the we saw in the [previous post]({{ root_url }}/blog/2015/07/03/scala-implicit-parameters/), we can maintain the elegant API.
  
{% codeblock lang:scala %}
implicit def waitForElement(locator: By)(implicit driver: WebDriver: WebElement = {
  val predicate: WebDriver => WebElement = _.findElement(locator)
  new WebDriverWait(driver, 30).withMessage(s"waiting for element '$locator' on page '${driver.getCurrentUrl}'").until(predicate)
}
{% endcodeblock %}

So the full example would look like this.

{% codeblock lang:scala %}
class ExampleWebDriverTest extends mutable.Specification {

  implicit var driver: WebDriver = Browser.create.driver

  "The 'save' button writes to the database" >> {
    val button = By.id("save")
    
    // scala calls the implicit def to convert the button into a WebElement
    button.click()        
    // ...
  }
}
{% endcodeblock %}


## Roundup

You can see from the examples above that implicit functions (and often combining them with implicit values) can make for succinct and more readable APIs.