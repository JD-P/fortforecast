# FORT FORECAST - DESIGN #

## Rationale ##

Fort Forecast is an experiment in social technology and [decentralized networking](https://github.com/redecentralize/alternative-internet)
in the vein of projects like [Urbit](http://urbit.org) or [Diaspora](https://en.wikipedia.org/wiki/Diaspora_%28social_network%29).
Where these projects implement a general social network for their users, Fort 
Forecast implements a specific community named Fort Forecast. The goals of Fort
Forecast as a project are:

- To develop useful analytics methods for managing online communities and test
the usefulness of keeping track of notable metrics such as churn rate of users 
and loss of regular members over time.

- To collect data about the growth and decay of online communities.

- To implement and survey the utility of the authors vision of an online community 
whose software is hand crafted towards the communities purpose.

- 

The goals of Fort Forecast as a community are:

- To help members improve their lives through the use and development of empirical
  effective methodology for their fields of endeavor.

- Be a 'force multiplier' for individuals who are working on interesting projects
  and seeking external motivation or assistance in completing them.

- 

----

## Concept ##

The original idea which inspired FortForecast was a loosely combined:

- Mailing List

- IRC channel meetups and coworking space

- Blogroll

Where the community would be centered around empirical approaches to hobbies and
more practical endeavors like career advancement or self experiment in the vein of
quantified self or [gwern branwen's](http://www.gwern.net/) self studies. 

The major problem with this approach was that it required a lot of effort from
various parties to make it fluid, and carried the built in baggage and stigma of
each service seperately even though in aggregate they represented different things.
FortForecast aims to be the opposite of this, the entire technology should make 
intended use and community norms as frictionless as possible.

FortForecast has a similar structure with very different implementation, the major
segments of the design are:

- A preemptive community charter which outlines expectations, rules, the purpose
of the community, who is prioritized in terms of competing access needs, etc. 
This will all be put in a version control system (Git) and married up with a 
version controlled set of precedents and institutional memories built up during
the first bans and ideally well oiled by the time that any sort of mass-ban machinery
is needed.

By doing this work up front, it will be much easier to justify needed bans and 
other moderator action without having to rehash the larger rationale behind these
descisions over and over perpetually.

- A new approach to forum software and threading which is based around tagging, 
summarization of threads, thread lineage as opposed to thread history (i.e, having
multiple iterations of the same thread instead of one long unreadable thread),
user discussion driven organization of 'boards' ('spools' in the FortForecast
forum metaphor), analytics, micro-moderation (many users holding many privileges
instead of a few users holding global privileges), and more.

- Unrestricted Jekyll blog hosting for every user, instead of expecting users to
all manage their own blogs. The document structure for this will be a lot like a
classical shell account web hosting setup. If a user would like to use an outside
hosting solution they can export their blog (as it will be plain Jekyll and 
therefore easy to migrate offsite given the data) and make their FortForecast 
blog homepage a redirect. Default styles, templates and CSS will be provided so 
that users who do not want to bother with such do not have to. Markdown will be 
a requirement to post.

- Robust featureful API, including risky untried features like letting other 
services import accounts from FortForecast with user permission. Ideally if 
another project like Urbit takes over FortForecast will be able to be imported
directly into it with little friction.

- Powerful site wide general analytics. Administrators should be able to gauge the
health of their communities, armed with information like how many regulars are
quitting over a given period of time or changes in the mood of the community.
This will also be an exercise in collecting information to analyze what happens
to communities that causes their decay. The administrator analytics will also
help put further checks and balances on moderator power.

- Prediction features as an integrated part of the site. Users will have a global
feed of predictions on their homepage with as associated RSS/Atom feed. When making
a post users will have the option of making a prediction which is added to their 
global feed. 

- Useful user homepages. Vbulletin does 'visitor comments'. Who *cares*? FortForecast
user pages will tell you what somebody has been working on, broadcast their time
spent working in things like pomodoro sessions, show their recent predictions,
give a sanctioned way to ask for/display contact information, broadcast 
commitments, and of course show biographical information like what time they
joined the site and their portrait at rest.

## Guidelines, Essays, Precedent ##

Rules are troublesome. When something is a *rule* that means it is forbidden in
all contexts and there is an obligation on the part of administrators and site
members to enforce it. (Or at least, this is the default assumption.) Guidelines 
by contrast allow more wiggle room, people can pass judgement with more nuance
and tell the rules-lawyer variety of pest that they have no power here.

So the site should have guidelines, and they should be short and to the point about
what behavior is expected from site members. They should be relatively non 
confrontational and try to cover a wide variety of cases without being too long
or so general that nothing can be blamed under them.

A more general philosophy should be espoused in a series of founding essays which
lay out in detail the rationale behind the community and the proposed management 
style. Most members are not expected to read these, though ideally most of your
founding members would.

While I'm not entirely sure at the time of writing exactly what topics these essays
should cover in their entirety, shoe-in subjects to appear are:

- An introduction explaining why start a community like FortForecast, what features
it will have and why it has them.

- 

The 

(Should at some point get to a *names* policy.)

## Implementation ## 

