Sensible JavaScript testing and some murders
============================================

:date: 2013-02-26 20:08
:summary: Notes from an Oslo XP Meetup about JavaScript testing, and a bonus
          talk.
:category: Programming
:tags: javascript, tdd, meetup, work culture

I was lucky to get a seat for the `first Oslo XP Meetup of 2013
<http://www.meetup.com/oslo-xp/events/104594972/>`_, helped in part by
GitHub [1]_. The topic was "Why does JavaScript testing have to be so DAMN
hard?", which is something I've been thinking about quite a bit lately
myself. Or rather, "how can I simplify the process of JavaScript testing and
avoid integration tests as much as possible?"

The presentation was given by `Magnar Sveen <https://twitter.com/magnars>`_
with examples from his work as a consultant at `FINN <http://finn.no/>`_.
Considering that he had to translate and run his whole presentation in
English [1]_ on short notice, he did a great job. Good examples, fun and
opinioned. Though as a future presenter myself I took note that I should
never, ever, put important things at the bottom of my slides. If need be,
add interstitiary slides that display the bottom parts higher up. Heads at
the front blocking people's view is bound to happen a lot.

The main point of his talk as I got it was to be a programmer, as opposed to
being a scripter, with his definition of this being to use abstractions. I
guess it's true, and I've been guilty of this myself, that a lot of JavaScript
"programmers" jump directly into implementing features quickly with the
powerful toolset jQuery gives. Without giving much thought about reusability
or… testing.

Magnars solution to this was focusing on writing "heavily tested, strictly
bounded, whiny components". His focus on components rather than a MVC mindset
is sensible, components simply being reusable and self contained objects. It
boils it down to the core of programming in JavaScript, rather than a more
specific model. Granted, Magnar didn't fancy the MVC model much in general for
JavaScript, but his point transcended that. But specifically for testing it
helps resolve the challenge with being so dependent on a DOM. If you write
components that are provided everything they need, including the DOM nodes,
you can write tests more easily without including large HTML structures.

But Magnars strangest idea, to me, was the whiny part of components. Well,
basically it just means that your components scream (throws exceptions) when
something you're supposed to provide them is missing. This is something I've
done myself, even as recently as this last weekend on a small project. But
Magnar takes this further into testing, suggesting we only write integration
tests on the combined uses of components and checking for no exceptions.
Putting components together is basically like writing mocks for testing, he
says. To keep your code DRY there's no use of writing separate tests for the
code that sets the components up, if you write heavily tested and whiny
components that throw exceptions when their requirements are not provided. An
interesting method and something I'll consider myself in the future.

After a short break from Magnars talk, a bonus talk by `Tim Berglund
<https://twitter.com/tlberglund>`_ of `GitHub <http://github.com/>`_ was
given. We were lucky enough to be the audience of Tims first ever (alpha)
public presentation of a talk he titled "First, Let's Kill the Product
Owners"[2]_. Having been to a few talks that was poorly presented I wouldn't
have thought this was Tims first presentation if this talk hadn't he
mentioned it, but that only speaks to Tims qualities as a public speaker.
The talk had a good flow, apart from an arcade throwing Tim off several
times with funny remarks, and Tim presented his thoughts very well.

My very first thoughts when Tim started his talk was "this aligns very well
with Valve's philosophy", something my colleague `Anders
<http:twitter.com/asteinlein>`_ brought up a while ago as a goal for our team.
Since this was a bonus talk, and the subject is quite deep, I'll keep this
summary brief: By eliminating managers, giving every employee ownership and
creative freedom, you'll end up with highly productive people that create more
value for your customers.

Specifically to this talk Tim was talking about Product Owners from an
`Agile <http://en.wikipedia.org/wiki/Agile_development>`_ view, meaning
business people with some technological knowledge, being responsible for
defining what should be developed and how that is detrimental to a developers
work. His example being a Product Owner asking a developer to pay no attention
to the user interface while developing an internal tool. And bugs? "We'll ship
with it, it's an internal tool." Which undermines any professional developer's
skills, basically saying that she should make something crappy.

Tim also brought up some typical excuses for not implementing this philosophy
and the problem of who'll choose the "crappy tasks" when everyone picks for
themselves what to work on. These were probably the points of his talk he
could need some input and experience from others on, but I agree with the gist
of it so far. Excuses are avoiding thinking about the problem thoroughly.
"Crappy tasks" are not worth doing if they don't serve any purpose, and tasks
that serve a purpose are not "crappy" by definition.

All in all this was a very good meetup, and I look forward to applying myself
even more at writing more testable JavaScript code (thus writing tests for
it), and evolving my company even further along the lines of Valve and GitHub.

.. [1] A couple of GitHub employees was by chance visiting Oslo, and Tim
    Berglund as one of them was given the opportunity to present a bonus
    talk for this meetup. This meant the event had to be moved slightly,
    colliding with some of the participants' calendar. It also meant that
    Magnar's talk had to be presented in English too.
.. [2] The title is, according to Tim Berglund, in reference to
    Shakespeare's `play about Henry VI`_ in which a rebellion against
    king Henry VI is executed by `Jack Cade`_. One of Jack's rebels says,
    in order to succeed with the plan: "The first thing we do, let's kill
    all the lawyers".
.. _play about Henry VI: http://en.wikipedia.org/wiki/Henry_VI,_Part_2
.. _Jack Cade: http://en.wikipedia.org/wiki/Jack_Cade
