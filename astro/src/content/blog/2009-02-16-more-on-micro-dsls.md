---
title: "More on Micro DSLs'"
pubDate: "2009-02-16'"
categories: 'java'
keywords: "dsl, domain specific langauges, micro-dsl, fluent api, java,"
description: "An example of a micro DSL to find items in a list using a fluent style API."
---

I was recently talking about what I call [micro DSLs](/blog/2009/01/06/be-more-expressive-with-builders/) and I thought I'd follow up with another example.

So, another example of a micro DSL I found myself writing is one of finding some object within a collection of differently typed objects. In my example, I want to find a `Race` object inside a bunch of calendar events objects, the finder micro DSL looks like this.

  
``` java
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
```

The way the class is built, it forces the client to use it such.


``` java
CalendarEventEntry event = find(race).in(events);
```

  
Where find is statically imported and race and events have been pre-populated.

  

The original version had a method in the class to do the find, in the context of this class it was harder to test the find. I had a bunch of mocks and I was testing the find function amongst other behaviours of the class. The search line looked something like this.

    
``` java
CalendarEventEntry event = searchForRaceIn(events);
```

## What's with "micro DSL"?

Why I term this a micro DSL is that it has a very specific usage (to find a race within a calendar) and it has a **private constructor** and **public static creation method** to ensure strict usage. The real thing though is the **method names don't really do what they imply they're going to do**. The `in` method actually does the search, but the `find` method doesn't do any such thing; it _creates_ an object.


> Micro DSLs are recognisable by their tiny-domain, the way in which construction is done to ensure methods can only be called in a certain order that makes sense to the domain and badly named methods.


How do you feel about this? When its used in a tiny domain like this and when it expresses the conversation more concisely than the alternatives, I feel pretty good about it. It makes me realise its not the words (method names) that are important, its the sentences they put together. So I'm compromising on realistic method names for more expressive sentences. The fact that the class prevents you from constructing invalid sentences just makes the warm feeling grow.

  
## Recommended Reading

<div>
    <script type="text/javascript">
    function trackOutboundLink(link, category, action) {

        try {
            _gaq.push(['_trackEvent', category , action]);
        } catch(err){}

        setTimeout(function() {
            document.location.href = link.href;
        }, 100);
    }
    </script>
</div>

<a href="http://www.amazon.co.uk/gp/product/1935182455/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1935182455&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">{% img right http://ecx.images-amazon.com/images/I/51KkyQcrsVL._SL160_.jpg 'DSLs in Action' %}</a>

<a href="http://www.amazon.co.uk/gp/product/0321712943/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=0321712943&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">{% img right http://ecx.images-amazon.com/images/I/51FwzT0U4LL._SL160_.jpg 'Domain Specific Languages (Addison-Wesley Signature)' %}</a>

 * <a href="http://www.amazon.co.uk/gp/product/0321712943/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=0321712943&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Domain Specific Languages (Addison-Wesley Signature)</a>, Martin Fowler
 * <a href="http://www.amazon.co.uk/gp/product/1935182455/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1935182455&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">DSLs in Action</a>, DSLs in Action
 * <a href="http://www.amazon.co.uk/gp/product/1934356999/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356999&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">The Definitive ANTLR 4 Reference: Building Domain-Specific Languages (Pragmatic Programmers)</a>, Terence Parr






