---
name: previewed
layout: post
title: JDK7 Previewed
time: 2011-03-04 15:44:00 +00:00
categories: java exceptions
comments: true
---

Oracle put out the preview release of JDK7 last month. I guess they felt they had to. So, it's not what was once heralded
(will [8 see lamdas](http://openjdk.java.net/projects/lambda/)?) but still has one or two interesting language features.
A few that caught my eye include...

### Type Inference on Generic Object Creation

  
Which allows a little brevity to the garrulity of the language, at least
against generic object instantiation where the type can be inferred. For
example,

{% codeblock lang:java %}
private Map<Size, List<Shoe>> stock = new HashMap<Size, List<Shoe>>();
{% endcodeblock %}

can be reduced to

{% codeblock lang:java %}
private Map<Size, List<Shoe>> stock = new HashMap<>();
{% endcodeblock %}

<!-- more -->

where the _diamond operator_ can be filled in or inferred from the
declaration. It's subtly different than leaving out the generic completely
which will reduce your type to being of `Object` Things don't get much better
than this.

  
Actually, it does. Just a little. Constructor generics always used to be fun
and that hasn't really changed, although with JDK7 you can do a little more.
For example,

{% codeblock lang:java %}
public class Bob<Y> {

    public <T> Bob(T t) {
    }

    public void example() {
        Bob<Integer> bob = new Bob<>("yum");
    }

    public void anotherExample() {
        Bob<Integer> bob = new <String> Bob<>("yum");
    }
}
{% endcodeblock %}

      
    

The examples are the same as the one Oracle gives, they both work with JDK7
only and show the `Integer` type inferred as the class generic (`Y`) in
combination with the diamond operator. The second example shows new syntax to
explicitly set type of the method generic and give some additional compile
time checks.

  

### try-with-resource and `AutoClosable`

  
Another bugbear with the verbosity of Java has always been the try-catch-
finally syntax. The new language feature try-with-resource allows you to chop
this down some what in combination with auto-closable resources. Here, rather
than the familiar, try-finally to close a resource, you can "open" the
resource within the parenthesis of the try statement (as long as the object
implements `AutoCloassable` and the resource will always close itself in a
`finally` like way.

  
For example,

{% codeblock lang:java %}
private String example() throws IOException {

    BufferedReader reader = new BufferedReader(...);

    try {
        return reader.readLine();
    } finally {
        reader.close();
    }
}
{% endcodeblock %}

      
gets replaced with

{% codeblock lang:java %}
private String example() throws IOException {
    try(BufferedReader reader = new BufferedReader(...) {
         return reader.readLine();
    }
}
{% endcodeblock %}

Dr Heinz combined this technique with a way to automatically unlock locked
resources in a [recent news letter](http://www.javaspecialists.eu/archive/Issue190.html).

There may be a little gotcha using this where exceptions can be suppressed and
have to be retrieved using `Throwable.getSuppressed()`. This seems like it
could be nasty.

### Catching Multiple Exceptions

  
This one allows you to catch multiple exceptions using a pipe to separate the
exception types. This looks like another work around for the general grips
with Java but removes the duplicated code you often get catching several
exceptions and treating them in the same way. For example,

{% codeblock lang:java %}
catch (IOException | SQLException e) {
    logger.log(e);
    throw ex;
}
{% endcodeblock %}

      
    

I usually end up pushing the code to execute as a `Callable` and dealing with
the exception in a lamda-like piece of code, or decorating the fragment to
deal with exceptions (logging or wrapping) or even trying really hard to throw
around runtime exceptions, so this one is at odds with my general approach.
Given the example from Oracle above, I suspect this will just facilitate ugly,
jammed in code. It seems to say "it's ok to deal with a bunch of exceptions in
the same way. in fact, we'll make it easier for you" without any warning about
if you actually _should_ be doing this type of thing. The fact the example
above (Oracle's example, by the way) logs then re-throws is a smell in it's
self. Perhaps I'm being premenstrual, but I'm not a fan of this one.

  
Have a look [here](http://download.java.net/jdk7/docs/#NewFeature) for on the
new features and download from
[here](http://www.oracle.com/technetwork/java/javase/downloads/ea-jsp-142245.html) (unfortunately, not for the Mac).

  
**UPDATE:** An extended version of this post has been published in
[May edition of the JavaTech Journal]({{ root_url }}/blog/2011/06/10/artcile-in-javatech-journal/).
  




