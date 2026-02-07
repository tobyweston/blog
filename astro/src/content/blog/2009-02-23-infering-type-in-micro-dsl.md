---
title: "Inferring the Types in a Micro DSL"
pubDate: "2009-02-23"
categories: 'java testing'
keywords: "dsl, fluent api, generics, java"
description: "Java can have trouble inferring multiple types, see and example and create a fluent API in Java using generics."
---

In a recent [post](/blog/2009/02/16/more-on-micro-dsls/), I was talking about a micro DSL to create a simple "find x in a list" service. The key thing here is that it defines how to look for x in the list. So the list can be a list of anything, not just a list of x's.
  
Just to recap then, to find something in a list, the original client code (using a static import) looks like this.

``` java
find(needle).in(haystack)
```

<!-- more -->
  
The class (in this case `NeedleFinder`) implements the DSL and specifically decides in the `in` method how to compare a `Needle` object to whatever is in the haystack list. I wanted to create a more generic class so started to implement the `ListFinder` to use generics and a couple of interesting things came out.

<!-- more -->
  
The generified class looks like this.

      
``` java
public final class ListFinder<T, L> {
    private final T target;
    private List<L> list = new ArrayList<L>();

    private ListFinder(T target) {
        this.target = target;
    }

    public static <T, L> ListFinder<T, L> find(T target) {
        return new ListFinder<T, L>(target);
    }

    public ListFinder<T, L> in(List<L> list) {
        this.list = new ArrayList<L>(list);
        return this;
    }

    public L using(Comparator<T, L> comparator) {
        for (L item : list) {
            if (comparator.equals(target, item)) {
                return item;
            }
        }
        return null;
    }

    public interface Comparator<T, L> {
        boolean equals(T target, L item);
    }
}
```

  
With the following test case showing its usage (the `Needle` and `Bale` class aren't show for brevity).

``` java
public class ListFinderTest {

    private final Needle needle = new Needle("Bob");
    private final Needle missing = new Needle("Billy");
    private final Bale bale1 = new Bale("Christian");
    private final Bale bale2 = new Bale("Bob in disguise");
    private final Bale bale3 = new Bale("Kelly");
    private final List<Bale> haystack = asList(bale1, bale2, bale3);

    private final ListFinder.Comparator<Needle, Bale> comparator = new ListFinder.Comparator<Needle, Bale>() {
        @Override
        public boolean equals(Needle needle, Bale bale) {
           return bale.name.contains(needle.name);
        }
    };

    @Test
    public void needleFoundInHaystack() throws Exception {
        assertThat(find(needle).in(haystack).using(comparator), is(bale));
    }

    @Test
    public void needleNotFoundInHaystack() throws Exception {
        assertThat(find(missing).in(haystack).using(comparator), is(nullValue()));
    }

    private static ListFinder<Needle, Bale> find(Needle value) {
        return ListFinder.find(value);
    }
}
```
## Equality
  
Here we're defining the equality of a `Needle` in a list of `Bale` objects to be when the name of a `Needle` is contained in the name of the `Bale`. A silly example I know but it illustrates that we redefine what we mean by equality for the list finder by implementing the `ListFinder.Comparator`. The concrete example that spawned the idea was when searching for a `Race` object inside a list of `Event` objects; two completely different entities.

## Type inference over too many types
  
Anyway, what I thought was interesting about this example was the type inference going on in the static find method. I originally wanted to just use `ListFinder.find` method directly as in the following.


``` java
ListFinder.find(needle).in(haystack).using(comparator)
```
    

  
Where `ListFinder` is statically imported. Usually, I'd rely on type inference here to work out that needle means `T` and therefore `T` is of type `Needle`. However, in the case above, the compiler will complain as the haystack parameter is not of type `Object`. The trick is that the generic method `find` in `ListFinder` needs to infer two types (`T` and `L`) but only has enough information for `T`. So it defaults `L` to type `Object`.

  
The alternative is to use the full notation as follows.

    
      
``` java
ListFinder.<Needle, Bale>find(needle).in(haystack).using(comparator)
```
  
Or (as I've done in the test) use an internal method who's return type gives the compiler enough information to infer both types. I prefer this approach as it makes the DSL expression to find a needle much more readable.


## Summary
  
So, Java can't chain methods to infer the types. I didn't really expect it to be able to so, its a bit much to ask for. Although it would be pretty sweet if it could.

  
One last thing, [Ray Barlow](http://codewax.blogspot.com/) was showing me a [Jedi](http://docs.codehaus.org/display/JEDI/Home) alternative to the finder. If we're lucky, he might blog about it. It seems Jedi offers some measure of residence against the proliferation of anonymous inner classes in lieu of closures but in all honestly, I just wanted to get in some big words in before
signing off. TTFN.

  
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

<a href="http://www.amazon.co.uk/gp/product/0321712943/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=0321712943&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">{% img right http://ecx.images-amazon.com/images/I/51FwzT0U4LL._SL160_.jpg 'Domain Specific Languages (Addison-Wesley Signature)' %}</a>

<a href="http://www.amazon.co.uk/gp/product/1935182455/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1935182455&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">{% img right http://ecx.images-amazon.com/images/I/51KkyQcrsVL._SL160_.jpg 'DSLs in Action' %}</a>

 * <a href="http://www.amazon.co.uk/gp/product/0321712943/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=0321712943&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Domain Specific Languages (Addison-Wesley Signature)</a>, Martin Fowler
 * <a href="http://www.amazon.co.uk/gp/product/1935182455/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1935182455&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">DSLs in Action</a>, DSLs in Action
 * <a href="http://www.amazon.co.uk/gp/product/1934356999/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356999&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">The Definitive ANTLR 4 Reference: Building Domain-Specific Languages (Pragmatic Programmers)</a>, Terence Parr



  
