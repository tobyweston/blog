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

In the previous post, we looked at implicit parameters; parameters that will be automatically passed values that have been marked as `implicit`. In this post, we'll take a look at implicit functions and how they can be useful to convert things of one type to things of another.

<!-- more -->

## Implicit Functions

Implicit functions will be called automatically if the compiler thinks it's a good idea to do so. What that really means is that if the code doesn't compile but would if a call was made to an implicit function, Scala will call that function to make it compile.


## Syntax


## Example

As an example, the fragment below uses [Web Driver](http://www.seleniumhq.org/projects/webdriver/) to wait for a UI element to appear on the screen (using a predicate based on `findElement`). It takes care of the typical problem whereby the element might not be available at the point you check for it; it smooths out some of the asynchronous issues you often get.

{% codeblock lang:scala %}
implicit def waitForElement(locator: By): WebElement = {
  val predicate: WebDriver => WebElement = _.findElement(locator)
  new WebDriverWait(driver, 30).withMessage(s"waiting for element '$locator' on page '${driver.getCurrentUrl}'").until(predicate)
}
{% endcodeblock %}


If we have a button that we'd like to find, we'd normally write something like (using a "locator" to locate it by `id` attribute).

{% codeblock lang:scala %}
  val button: WebElement = driver.findElement(By.id("save-button")
  button.click()
{% endcodeblock %}

It'd be nice if we could shorten down the call and at the same time get the `findElement` call retrying if it's not yet there. 

We can create an instance of the "locator" and rather than call `driver.findElement` directly, we can write something like the following.

{% codeblock lang:scala %}
  val button = By.id("save-button")
  button.click()
{% endcodeblock %}  

Without the implicit `waitForElement` function, the code wouldn't compile. `By` doesn't have a `click` method on it. With the implicit function in scope, the compile can work out that if it calls it passing in `create` as the argument, the return type _would_ have a `click` method and so compile. It does the wiring for you giving you an elegant API.

Now there's one little bit I've brushed over here; how is the `WebDriver` `driver` instance available? The example above just assumes its available but it'd be nicer to pass it into the function along with `locator`. However, there's a restriction of passing only a single argument into an implicit function. The answer is to use a second argument (using Scala's built in currying support). By combining implicit parameters the we saw in the [previous post]({{ root_url }}/blog/2015/07/03/scala-implicit-parameters/), we can maintain the elegant API.
  
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

  "Save writes to the database" >> {
    val button = By.id("save")
    
    // scala calls the implicit def to convert the button into a WebElement
    button.click()        
    // ...
  }
}
{% endcodeblock %}


## Roundup
