---
name: more-on-micro-dsls
layout: post
title: More on Micro DSLs
time: 2009-02-16 20:06:00 +00:00
categories: java
comments: true
---

I was recently talking about what I call [micro DSLs](http://baddotrobot.com/blog/2009/01/06/be-more-expressive-with-builders/) and I thought I'd follow up with another example.

So, another example of a micro DSL I found myself writing is one of finding
some object within a collection of differently typed objects. In my example, I
want to find a `Race` object inside a bunch of calendar events objects, the
finder micro DSL looks like this.

  
{% codeblock lang:java %}
final class RaceFinder {

    private final Race race;

    private RaceFinder(Race race) {
        this.race = race;
    }

    static RaceFinder find(Race race) {
        return new RaceFinder(race);
    }

    CalendarEventEntry in(List<CalendarEventEntry> events) {
        for (CalendarEventEntry event : events) {
            if (race.getName().equals(event.getTitle().getPlainText())) {
                return event;
            }
        }
        return null;
    }
}
{% endcodeblock %}


The way the class is built, it forces the client to use it such.


{% codeblock lang:java %}
CalendarEventEntry event = find(race).in(events);
{% endcodeblock %}


  
Where find is statically imported and race and events have been pre-populated.

  

The original version had a method in the class to do the find, in the context
of this class it was harder to test the find. I had a bunch of mocks and I was
testing the find function amongst other behaviours of the class. The search
line looked something like this.

    
{% codeblock lang:java %}
CalendarEventEntry event = searchForRaceIn(events);
{% endcodeblock %}


  

Why I term this a micro DSL is that it has a very specific usage (to find a
race within a calendar) and it has a private constructor and public static
construction method to ensure strict usage. The real thing though is the
method names don't really do what they imply they're going to do. The `in`
method actually does the search, but the `find` method doesn't do any such
thing; it _creates_ an object.

  

How do you feel about this? When its used in a tiny domain like this and when
it expresses the conversation more concisely than the alternatives, I feel
pretty good about it. It makes me realise its not the words (method names)
that are important, its the sentences they put together. So I'm compromising
on realistic method names for more expressive sentences. The fact that the
class prevents you from constructing invalid sentences just makes the warm
feeling grow.

  

> Micro DSLs are recognisable by their tiny-domain, the way in which
construction is done to ensure they can only be called in an order that makes
sense to the domain and badly named methods.


Micro DSLs are starting to spread in my code like jam on toast but I know I
have to check myself and really justify their use before I go mad. I also had
fun trying to turn the finder above into a generified class which I'll talk
about in my next post. I bet you can't wait, you lucky people.



