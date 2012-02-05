---
name: inheritance-vs-composition
layout: post
title: Inheritance vs Composition
time: 2009-01-24 12:12:00 +00:00
categories: java object-oriented
---

When interviewing, I often like to ask a candidate to discuss inheritance vs composition using a `Stack` as an example.
  

### Example 1.

{% codeblock lang:java %}
public class EvilStack<T> extends Vector<T> {
    public T pop() {
        // ...
    }
    public void push(T item) {
        // ...
    }
}
{% endcodeblock %}


### Example 2

{% codeblock lang:java %}
public class Stack<T> {
    private Vector<T> items = new Vector<T>();
    public T pop() {
        // ...
    }
    public void push(T item) {
        // ...
    }
}
{% endcodeblock %}


  
Extending `Vector` as in example 1 weakens the encapsulation of the class.
Suddenly, methods to get and insert elements at specific positions are
available to clients of the stack. We move from trying to create a well
behaved LIFO stack to creating a socially irresponsible monster: an `EvilStack`.

  
So I was surprised when looking at the Java source to see that
`java.util.Stack` actually extends `Vector`! Naughty.

  
{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/SVInGoVdYJI/AAAAAAAAC08/I4RV1KzCyPo/s320/gibble_22x22.png %}

