---
title: "Be Explicit with the UI Thread"
pubDate: "2008-12-30"
categories: 'java testing concurrency'
keywords: "SWT, UI thread, event dispatching thread, EDT, invalid thread access, Display.sync, Display.async"
description: "Understand the SWT UI thread and how to avoid invalid thread access errors by being explicit about which thread is the main UI thread when testing."
---

Following up from the post [SWT Support in Window Licker](/blog/2008-12-29-swt-support-for-window-licker/).
  
The thing I found most interesting about looking at this was having to be more explicit about the UI thread. When developing SWT applications, we're all aware that accessing almost anything graphical in SWT from any other thread than the UI thread spells "invalid thread access", but it was fun to be more explicit about the "UI thread".

  
When I started to look at how I go about writing SWT applications, I noticed that

  * I often run the application from a `main` method somewhere which runs on the `main` thread.
  * I often discover invalid thread access problems at run time.
  * I often plug the problem by wrapping the offender in a `Display.sync(...)` or `Display.async(...)` call.
  * I often have very few long running processes that need to spawn a thread and update the UI.  

It wasn't until I started looking at being able to run the application from the context of a JUnit test that I started to think in more detail about these.

  
## Running the application from a main method

This seems simple but being more explicit about the UI thread means that this is worth a closer look. I always used to start an SWT application from the `main` method, in variations of the code below.

  
``` java
public class SwtCalculator {
    public static void main(String... args) {
        new SwtCalculator();
    }

    public SwtCalculator {
        display = Display.detDefault();
        shell = new Shell(display);
        shell.setText("Calculator");
        // shell setup
        startEventLoop();
    }

    public void startEVentLoop() {
        while (!shell.isDisposed()) {
            if (!display.readAndDispatch())
                display.sleep();
        }
        display.dispose();
    }
}
```
The default constructor would do or delegate the work to setup the various shells and widgets and finally start the event loop. When using JFace's `ApplicationWindow`, I'd do pretty much the same thing. Calling `window.setBlockOnOpen(true)` just shifts the responsibility of starting the event loop to the `ApplicationWindow class`. If you call `window.setBlockOnOpen(false)` for example, you have to manually start an event loop.

  
However you do it, getting into that event loop blocks the client and **it's the thread that executes this event loop that is called the UI thread**. It just so happens that most SWT applications will hit that loop from the main thread as you can see from the following partial thread dump.


    Name: main
    State: RUNNABLE
    Total blocked: 0 Total waited: 0

    Stack trace:
        org.eclipse.swt.internal.win32.OS.WaitMessage(Native Method)
        org.eclipse.swt.widgets.Display.sleep(Unknown Source)
        com.objogate...SwtCalculator.startEventLoop(SwtCalculator.java:104)
        com.objogate...SwtCalculator.main(SwtCalculator.java:113)

  

At this point, the SWT event loop is doing its thing, waiting for UI events (mouse clicks, keyboard input etc) and dispatching them to the appropriate listeners. So, we can define what we mean by the UI thread;

> The UI thread or event dispatching thread is the thread that executes the standard SWT event loop.


## Running the tests and GUI in different threads

  
So, if the event loop was called from within say a `@Before` annotated method in a test, the test would block until the event loop finished, the display would be disposed and any subsequent tests against the GUI elements would quickly discover that they no longer exist.

It should be pretty clear then that in order to test GUI elements the event loop has to be started in a different thread than the tests run in. The gotcha is that the test thread will likely want to interact with this UI thread in order to push buttons and make assertions and that's when we get into invalid thread access territory with SWT.

  
The way I implemented this was to use a class extending `Thread` to represent the UI thread and to start the event loop in its `run()` method. The tests can interact with the UI thread by either searching for the display with `Display.findDisplay(thread)` or by cooperating and ensuring that only the default display is used (retrieving it using `Display.getDefault()`).

  
A minor change to the application's main method is required to optionally not call the event loop when calling main. For example;

``` java
public static void main(String... args) {
    SwtCalculator calculator = new SwtCalculator();
    if (shouldBlock(args))
        calculator.startEventLoop();
}
```
The tests can then explicitly create a UI thread delegating shell setup to the `SwtCalculator` class before starting the event loop and allowing the test thread to continue.

``` java
@Before
public void runTheApplication() {
    thread = UIThread.startNewUIThread(new UISetupClosure() {
        public void performAdditionalSetup() {
            SwtCalculator.main(DONT_BLOCK_ON_OPEN);
        }
    });
    ui = new SwtCalculatorDriver();
}

@Test
public void calculatorCanAddTwoNumbers() {
    // testing the calculator whilst the main thread is running and
    // the UI has been started in another thread (from @Before)
}

@After
public void stopTheApplication() {
    thread.interrupt();
}
```

The `UISetupClosure` allows the setup code (in this case the main method) to run inside the UI thread. This uses the strategy pattern but an alternative design could just as easily sub-class the `UIThread` and use the template pattern in a similar way.

  
The interrupt allows the event loop on the UI thread to be interrupted and stop gracefully.

  
The following partial thread dump shows it in action. As you can see, an explicit thread has started the event loop (the `Display.sleep` and `WaitMessage`
are the hints).

  
    Name: SWT-Event-Dispatcher-Thread-1
    State: RUNNABLE
    Total blocked: 0 Total waited: 0

    Stack trace:
        org.eclipse.swt.internal.win32.OS.WaitMessage(Native Method)
        org.eclipse.swt.widgets.Display.sleep(Unknown Source)
        com.objogate.wl.swt.UIThread.startEventLoop(UIThread.java:90)
        com.objogate.wl.swt.UIThread.run(UIThread.java:68)
        - locked java.lang.Class@1d7fbfb

  
It was a good exercise exploring the UI thread and I encourage you to take a look at [Window Licker](http://code.google.com/p/windowlicker/) (and my [SWT patch](http://windowlicker-users.googlegroups.com/web/window-licker-swt-spike.patch)). Have a play and see if you agree with the approach I took above.

  


