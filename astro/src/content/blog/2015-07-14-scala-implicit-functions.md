---
title: "Implicit Functions in Scala"
subTitle: "Master automatic type conversions and write more succinct APIs"
pubDate: '2015-07-14'
categories: 'scala'
keywords: "scala, implicit, implicit function, implicit conversion, SAM, implicits"
description: "Implicit functions, their usages and examples. Learn how implicit functions help make your APIs more succinct, reduce your code and convert types."
series: 'Scala Implicits'
---

In the [previous post](/blog/2015-07-03-scala-implicit-parameters/), we looked at implicit parameters; parameters that will be automatically passed values annotated as `implicit`. In this post, we'll take a look at implicit functions and how they can be useful to convert things of one type to things of another.


## Implicit Functions

Implicit functions will be called automatically if the compiler thinks it's a good idea to do so. What that means is that if your code doesn't compile but would, if a call was made to an implicit function, Scala will call that function to make it compile. They're typically used to create _implicit conversion functions_; single argument functions to automatically convert from one type to another.

For example, the following function allows you to convert a Scala function into a instance of the Java 8 `Consumer` [single argument method](/blog/2014-04-07-functional-interfaces-in-java8/) but still use Scala's concise syntax. 

``` scala
implicit def toConsumer[A](function: A => Unit): Consumer[A] = new Consumer[A]() {
  override def accept(arg: A): Unit = function.apply(arg)
}
```
You can avoid having to write clunky anonymous class instantiation when interfacing with Java and so mimic Java's lambda syntax. So rather than having to use the longhand version like this. 

``` scala
def exampleUsingJavaForEach() {
  javaCollection.forEach(new Consumer[Element]() {
    override def accept(element: Element): Unit = observer.update
  })
}
```
You can write this, where we just pass a Scala function to Java's `forEach` method.
 
``` scala
def exampleUsingImplicitConversion() {
  javaCollection.forEach((element: Element) => observer.update)
}
```
The argument to `forEach` is actually a function of type `Element => Unit`. Scala recognises that the `toConsumer` method could convert this into a `Consumer[Element]` and does so implicitly.     

``` scala
def exampleUsingImplicitConversion() {
  val function: ObserverS => Unit = (observer) => observer.update
  javaCollection.forEach(function)
}
```
Which is basically shorthand for this.

``` scala
def exampleUsingImplicitConversion() {
  val function: ObserverS => Unit = (observer) => observer.update(this, status)
  javaCollection.forEach(toConsumer(function))
}
```
  
## Another Example

If we have a button on we web page that we'd like to find using [Web Driver](http://www.seleniumhq.org/projects/webdriver/), we'd normally write something like the following, using a "locator" to locate it by `id` attribute.

``` scala
  val button: WebElement = driver.findElement(By.id("save-button")
  button.click()
```
It doesn't take into account that the element might not be there when we call it (for example, when our UI uses ajax and adds the button asynchronously) and it's also a bit verbose. We can use an implicit function to address both of these issues.

The fragment below uses the [`WebDriverWait`](https://selenium.googlecode.com/git/docs/api/java/index.html?org/openqa/selenium/support/ui/WebDriverWait.html) class to wait for a UI element to appear on the screen (using `findElement` to check and retrying if necessary) and so smooths out the asynchronous issues.

``` scala
implicit def waitForElement(locator: By): WebElement = {
  val predicate: WebDriver => WebElement = _.findElement(locator)
  new WebDriverWait(driver, 30).withMessage(s"waiting for element '$locator' on page '${driver.getCurrentUrl}").until(predicate)
}
```

It's also an implicit function designed to convert a `By` locator into a `WebElement`. It means we can write something like the following where `button` is no longer a `WebElement`, but a `By`.

``` scala
  val button = By.id("save-button")
  button.click()
```  

Without the implicit `waitForElement` function, the code wouldn't compile; `By` doesn't have a `click` method on it. With the implicit function in scope however, the compiler works out that calling it (and passing in `create` as the argument), would return something that _does_ have the `click` method and would compile. 

## Single Arguments Only Please

Now there's one little bit I've brushed over here; namely how the `WebDriver` `driver` instance is made available. The example above assumes it's available but it'd be nicer to pass it into the function along with `locator`. However, there's a restriction of passing only a single argument into an implicit function. The answer is to use a second argument (using Scala's built in [currying support](/blog/2013/07/21/curried-functions/)). By combining implicit parameters the we saw in the [previous post](/blog/2015/07/03/scala-implicit-parameters/), we can maintain the elegant API.
  
``` scala
implicit def waitForElement(locator: By)(implicit driver: WebDriver: WebElement = {
  val predicate: WebDriver => WebElement = _.findElement(locator)
  new WebDriverWait(driver, 30).withMessage(s"waiting for element '$locator' on page '${driver.getCurrentUrl}").until(predicate)
}
```
So the full example would look like this; making `driver` an implicit `val` means we can avoid a call to `button.click()(driver)`.

``` scala
class ExampleWebDriverTest extends mutable.Specification {

  implicit val driver: WebDriver = Browser.create.driver

  "The 'save' button writes to the database" >> {
    val button = By.id("save")
    
    // scala calls the implicit def to convert the button into a WebElement
    button.click()        
    // ...
  }
}
```

## Roundup

You can see from the examples above that implicit functions (and often combining them with implicit values) can make for succinct and more readable APIs. Next we'll look at implicit classes.

If you're interested in more Java bridge implicits like `toConsumer`, check out this [gist](https://gist.github.com/tobyweston/0fbb8eb114db48596e6b).