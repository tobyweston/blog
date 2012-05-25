---
name: logging-is-evil-but
layout: post
title: Logging is evil but...
time: 2010-10-18 20:51:00 +01:00
categories: java mocking testing exceptions rest
comments: true
sidebar : false
---

Logging is a nightmare. I don't mean here that conveying information about
exceptional circumstances is a nightmare, I mean the combination of over eager
developers and [_insert your current logging framework here_] is a recipe
for disaster. We've all seen too much of


{% codeblock lang:java %}
Logger log = Logger.getLogger(ThisSucks.class);
...
try {
    somethingRisky();
} catch (SomethingVeryBadException e) {
   log.error(e);
   throw e;
}
{% endcodeblock %}


which is just one example where the exception handling policy for the system
(it's a system-wide concern remember) is muddled at best. Nothing is saying
that the same exception isn't logged elsewhere or that the exception is even
handled correctly or the right people notified. It's not ok to just log and
rethrow and every single time we go to declare a new logger, we should think
twice.

<!-- more -->

We've taken this very literally in my current project and everyone is actively
discouraged from instantiating a logger. I'd rather be explicit that some
exception event has occurred and fire an event that some interested party can
listen for. This makes perfect sense when you think about the huge log files
that someone has to trawl through, armed only with for some vague clue as to
what went wrong, a grep manual and the futile hope that developers actually
log something useful. All without the context of the code to actually guide
them. Good luck.

The disseminated log problem is exacerbated if there is no clear audit trail
tying pieces of information together. In a system with thousands of request
per second, how do you tie the logged request inputs to some stack trace
embedded in the middle of another thousand requests? What should have been a
clear set of requirements from the business (in this case, presumably the
support team) can easily get lost in the technical translation.

> Logging is evil, but if you really *have* to, be honest about it...

Asking the business _"what information do you want to see in the event of x
happening"_ rather than assuming they want to see some stack trace in a huge
log can make a lot of sense. We're often not logging for ourselves (we have
debuggers for that), we're often logging for our customers. If we start to
think about this stuff early, in terms of exception events and their audience,
we can build systems that tell the outside world something meaningful in
flexible ways. We start to define a system wide exception handling policy
rather than relying of the default exception handler (`System.out` is rarely
the right choice!).

So back to my current project... people are regularly beaten with a chair leg
for creating loggers but I'll admit that on occasion, I've actually logged
stuff and didn't resort to some Opus Dei style self-flagellation. Logging is
evil, but if I really *have* to log, my saving grace is to be explicit about
it. I'll hunt down a customer and I'll write a test to advertise the fact the
log contains what they asked for.

Most of the common logging frameworks make it troublesome to inject a logger
instance, and I'm reluctant to subvert behaviour just because some logging
framework wants me to. Logging (or preferably, firing an event) should be
orthogonal to the classes core behaviour, why should I compromise? My
preferred approach is the canonical example of using Aspects, or less
esoterically, using decorators.

For example, I created a interface to handle HTTP POST requests, imaginatively
called `Post`. Why should I add logging to implementations and open the door
to ad-hoc, erratic logging? I shouldn't, but when my implementation
`CustomerPost` requires logging of the request and response, I can decorate
with a `LoggingPost`


{% codeblock lang:java %}
public class LoggingPost implements Post {

    private static final Logger LOG = Logger.getLogger(Post.class);

    public LoggingPost(Post delegate) {
        this.delegate = delegate;
    }

    @Override
    public Response post(Body body) {
       try {
           return delegate.post(body);
       } catch (IOException e) {
           LOG.error(e.getMessage(), e);
           throw e;
       }
    }
}
{% endcodeblock %}


You might be concerned that the try/catch above looks very similar to the
original negative example. The good thing about our decorated example above is
that by being explicit about this classes responsibility, declaring the usage
in the correct context, we can actually define the system wide policy for
logging the `Post` calls in one place, without affecting the contract of the
interface. We'd do this for example, on the system boundary, for example where
the RESTful API is implemented.

{% codeblock lang:java %}
@Resource
public class CustomerServlet {

    public void doPost(Request chuck, Response up) {
        ...
        customer = new LoggingPost(new CustomerPost(...));
        customer.post(...)
        ...
    }
}
{% endcodeblock %}

In our `LoggingPost` above, we haven't even tried to inject a logger in to
make the testing easier. Instead, mostly because I was being lazy, I used the
helper class below. This is intended to represent Log4J in the context of a
test and give access to the logger for assertion purposes.

{% codeblock lang:java %}
public class Log4J {

    private final StringWriter writer = new StringWriter();
    private final Logger logger;
    private final String uuid = UUID.randomUUID().toString();

    public static Log4J appendTo(Logger logger) {
        return new Log4J(logger);
    }

    private Log4J(Logger logger) {
        this.logger = logger;
        WriterAppender appender = new WriterAppender(new SimpleLayout(), writer);
        appender.setName(uuid);
        logger.addAppender(appender);
    }

    public void clean() {
        logger.removeAppender(uuid);
    }

    public void assertThat(Matcher<String> matcher) {
        org.junit.Assert.assertThat(writer.toString(), matcher);
    }
}
{% endcodeblock %}

Using it in the test for `LoggingPost` is shown below

{% assign braces = '{{' %}
{% codeblock lang:java %}
@RunWith(JMock.class)
public class LoggingPostTest {

    private final Mockery context = new Mockery();
    private final Post mock = context.mock(Post.class);
    private final Log4J logger = Log4J.appendTo(Logger.getLogger(Post.class));

    private static final String EXCEPTION_MESSAGE = "bar bar black sheep...";

    @Test
    public void shouldDelegate() throws Exception {
        context.checking(new Expectations() { {
            one(mock).post(...);
        }});
        new LoggingPost(mock).post(...);
    }

    @Test
    public void shouldLogWhenExceptionIsThrown() {
        try {
            postWill(throwException(new IOException(EXCEPTION_MESSAGE)));
            new LoggingPost(mock).post(...);
            fail();
        } catch (IOException e) {
            logger.assertThat(allOf(containsString("ERROR"), containsString(EXCEPTION_MESSAGE)));
        }
    }

    @After
    public void cleanupLogger() {
        logger.clean();
    }

    private void postWill(final Action action) {
        context.checking(new Expectations(){{ braces }}
            allowing(mock); will(action);
        }});
    }
}
{% endcodeblock %}

It relies on nasty statics to dynamically add a logger to Log4J's list of
loggers and thereby appending any generated logs to something that the `Log4J`
test helper can assert on. I can't decide if I like this or not. It gives you
an extra test that your class under test is using a logger with the name that
you expect (`"Post.class"` in the example above), testing your logger
configuration as a by-product.

What I found interesting about this though was that it was always seemed a lot
of effort making some logging framework play nicely with mocks, or writing and
configuring a custom in memory appender and asserting on it. With the above
example, I very quickly added confirmation to existing Log4J infrastructure.
It seemed almost too easy... so I'd love to hear your comments and how you
write tests for logging.

PS. Logging is evil.


