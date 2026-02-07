---
title: "Tail Recursion Optimisation in Scala"
pubDate: '2013-07-16'
categories: 'java scala'
keywords: ""
description: "Scala can optimise recursive calls where the last statement in a method is a recursive one. In this post we'll have a look at what this means and why call tail optimisation is useful. Along the way, we'll also discuss infinite tail recursion."
published: false
---

Scala can optimise recursive calls where the last statement in a method is a recursive one. In this post we'll have a look at what this means and why call tail optimisation is useful. Along the way, we'll also discuss infinite tail recursion.

<!-- more -->

Typical recursive calls will have to build a stack frame for every recursive invocation. At the point a method calls itself, it will have to store all state in the current frame, create a new frame and push it onto the stack. It can then transfer control to the new invocation. When the newly executed method returns, the current frame can be popped off and the program can continue from where it left off.

This all takes effort and memory. When it all becomes too much, we'd get a `StackOverflowError`.

If we look at the following object (adapted from Odersky) and it's recursive method `tick`, we can see this process in action.

``` scala
  object Bomb {
    def tick(countdown: Int): Int = {
      if (countdown == 0) throw new Explosion("BOOOOM!")
      else tick(countdown - 1) + 1
    }
  }
```

When you run this with

``` scala
  Bomb tick(3)
```

You'll see the following stack trace

    RecursionTest$Explosion: BOOOOM!
        at RecursionTest$Bomb$.tick(RecursionTest.scala:7)
        at RecursionTest$Bomb$.tick(RecursionTest.scala:8)
        at RecursionTest$Bomb$.tick(RecursionTest.scala:8)
        at RecursionTest$Bomb$.tick(RecursionTest.scala:8)

Each line in the stack trace represents a frame.

If we modify the `tick` method to ensure that the last statement is a recursive call by dropping the pointless `+ 1` statement, Scala should recognise the fact that the method is tail recursive and can optimise it. It needs a little help with the `@tailrec` annotation however.

``` scala
  object Bomb {
    @tailrec
    final def tick(countdown: Int): Int = {
      if (countdown == 0) throw new Explosion("BOOOOM!")
      else tick(countdown - 1)
    }
  }
```

Which would output the following stack trace

    RecursionTest$Explosion: BOOOOM!
        at RecursionTest$Bomb$.tick(RecursionTest.scala:7)


## Recursive

```
  public int tick(int a) {
    iload 1
    iconst_0
    if_icmpne l0
    _new 'java/lang/Exception'
    dup
    ldc "BOOOOM!"
    invokespecial 'java/lang/Exception.<init>','(Ljava/lang/String;)V'
    athrow
   l0
    aload 0
    iload 1
    iconst_1
    isub
    invokevirtual 'RecursionTest.tick','(I)I'
    iconst_1            // push 1
    iadd                // pop and add
    ireturn
  }
```

## Call tail optimisation

```
  public final int tick(int a) {
   l0
    iload 1
    iconst_0
    if_icmpne l1
    _new 'java/lang/Exception'
    dup
    ldc "BOOOOM!"
    invokespecial 'java/lang/Exception.<init>','(Ljava/lang/String;)V'
    athrow
   l1
    iload 1
    iconst_1
    isub
    istore 1
    _goto l0            // this is the good bit
  }
```

Reverse engineering this from the byte code to Java, shows the optimisation long hand.

``` java
public final int tick(int countdown) {
 while (true) {
   if (countdown == 0)
      throw new Exception("BOOOOM!");
   countdown -= 1;
 }
}
```

### Resources

* http://blog.richdougherty.com/2009/04/tail-calls-tailrec-and-trampolines.html
* http://docs.oracle.com/javase/specs/jvms/se7/jvms7.pdf
* http://stronglytypedblog.blogspot.co.uk/2009/08/scala-tail-recursion.html