# APIs and RESTfulness

Up to this point, we’ve been creating some web apps using Pyramid or Django.
Each of the web apps has had a front-end of some sort, many borrowing
liberally from template sites like Zurb Foundation or Bootstrap. However, we
don’t learn Python so that we can make pretty front-end sites.

We learn and write Python so that we can efficiently and sensibly control the
back-end processes that put websites into production. It shouldn’t matter what
our front-end looks like. We process input and deliver data, and we do so via
an API.

## What is an API?

**API** stands for **A** pplication **P** rogramming **I** nterface. As the
name implies, it is the interface that sits between the application (e.g. the
front-end or client-side of your app) and the back-end (e.g. where the data is
housed). An API embodies all of the functionality of your app: what can be
created and deleted, what can be displayed and how to display it, how
navigation works, etc. For our Django and Pyramid applications, our API has
been embodied by our Views and URLs.

We’ve also thrown around the word API a lot with respect to our data
structures assignments. Really, all that means is the set of functionality
that’s available to the user of the code that we’re producing. So, our `Queue`
API allows a user to set up data to be removed and inspected in the order in
which it was inserted. Our `Graph` API lets us store information as a set of
nodes and relations, that we can then traverse and find paths between. Our
`Trie Tree` API allows us to store words as branches of alphabetical stubs,
and allows us to retrieve words (and even in some cases use it for auto-
completion of a word stub).

With Pyramid we had a specific example of our API having two different ways of
being visualized. Our main means came in the form of HTTP responses returning
rendered HTML, which was provided for a specific URL route. We also had routes
and views that returned information in the form of JSON ( **J** ava **S**
cript **O** bject **N** otation). This was so that some external HTTP request
could access raw data, without all of the frills and trappings of rendered
HTML and CSS. It was just pure text. In the web world, this view is what is
most often thought of as an application’s API, and provides a simple means for
machines (or applications) to talk to each other in simple, easily-parsed
ways.

There are many types of web app APIs. Two main ones set standards and rule the
pack: **SOAP** and **REST**

### SOAP

**S** imple **O** bject **A** ccess **P** rotocol is a separate protocol,
distinct from HTTP (though was often used over HTTP). SOAP is a set of
instructions, typically sent as XML (slow to parse, and lacking more universal
standards) that allow for...simple object access. The responses would also
come back as XML, with object attributes set out in parseable XML tags.

SOAP interactions would happen via `GET` requests. Each `GET` would act on an
endpoint that would retrieve or modify data. For example:

  * `GET /images/get-photo`
  * `GET /images/get-photos`
  * `GET /images/add-photo`
  * `GET /images/edit-photo`
  * `GET /images/delete-photo`

That data would then be returned as XML which would then need to be parsed
apart and used for whatever. We will not be using this.

## RESTful APIs

The modern standard for application APIs is REST: **RE** presentational **S**
tate **T** ransfer. It’s concerned most with scalability and portability of
web applications, seeking to increase visibility and decrease dependencies
between the back-end and front-end.

Instead of interacting with an application with a focus on routes, REST
focuses instead on the resources (objects) themselves. It uses HTTP verbs to
interact with those objects, just like we would with an HTML form. For
example:

  * `GET /images/photos/:id`
  * `GET /images/photos`
  * `POST /images/photos`
  * `PUT /images/photos/:id`
  * `DELETE /images/photos/:id`

The result would then be returned as JSON, which would also then need to be
parsed and used for whatever. That’s great and all, but what differentiates a
REST API from any other API?

### 5+ Constraints of a RESTful API

In order for an API to be considered a REST API, it must adhere to the
following constraints:

  * it must separate client interactions from server interactions
  * be stateless
  * enable cacheing of page results
  * present a uniform interface between components
  * enable a layered system architecture

It can also optionally allow for code on demand. Let’s dig into each of these
a bit.

#### Client-Server Separation of Concerns

We’ve separated HTML from CSS, we’ve separated views from routes from
templates from models. We’ve seen that when you focus a script on one thing,
you can actually manage to do that one thing well. A similar notion is
employed here.

The back-end shouldn’t have to consider anything about how the front-end is
designed. The entire focus of a web app’s back-end is on the storage and
processing of information.

Similarly, the front-end (client side) shouldn’t have any concern about how
the back-end stores or processes information. Its only focus should be on the
user interface and user experience. It should expect data to be accessible,
and provide all of the configuration needed in order to retrieve it from the
back-end.

This separation allows for the client-side and the server-side to evolve
completely independently. In fact, as long as the basic functionality is
preserved, the front-end and the back-end could more or less be two entirely
separate applications. This is why you’ll often see Django in job postings
with AngularJS or ReactJS. Those front-end frameworks don’t need to care where
the data is coming from, they just need to have data to present. Similarly,
the back-end can scale up, scale down, or add new features and not worry about
how it affects the front-end as long as the basic functionality expected by
the front-end is preserved.

#### Statelessness

As a part of the client-server separation of concerns, the back-end doesn’t
concern itself with the client’s state (or by extension the user’s state).
This means that no session information, nor any cookies need be stored on the
server-side. As far as the server is concerned, every request from the client-
side is fresh and brand new, containing all of the information that is needed
to make the request it wants. This includes things like authentication keys.

An advantage of statelessness is reduced load on the server side, and by
extension a more scalable back-end. Session state is inherently small in size.
However, one can imagine that an application with thousands, millions, or
billions of users may see the server load spike up and response speed slow
down as a result. This way, the only thing that the server need do is handle
the request. This also means that any machine that’s serving the same site
that can handle the request can return the appropriate response, without
having to pass around session information about client state.

There is a trade-off here. Putting the responsibility of maintaining client
state on client side requires the trust that the client side can always handle
its own state well, across software updates and different client
architectures. It also means that repetitive requests may have to be made for
the same resources, instead of having something saved on the server side as a
shortcut for that state.

#### Cacheing

Cacheability refers to the ability for an often-used resource response to be
stored client-side for quick access, instead of having to run through the
entire web request-response cycle in order to retrieve that information. This
constraint doesn’t require that every HTTP response be cached on the client-
side. All that this means is that the _possibility_ exists for certain
responses to be labeled as cacheable or non-cacheable.

The benefit of a cacheable respones is that it removes some client-server
interactions. The fewer interactions, the faster the response. The faster the
response, the better the performance of the application. Also, the easier it
is to scale the app instead of having to worry about server load.

The downside is that you have to be careful about what you allow to be
cacheable. The reliability of the data in the response is compromised if stale
data differs significantly from what would be returned by a full request to
the server. The remedy of course is to be mindful of what is and isn’t
cacheable from your API.

  * CSS files? Definitely cacheable.
  * JS files? Probably cacheable.
  * Image files that are a part of your site’s design? Probably cacheable.
  * Rendered HTML responses? Not likely.

#### Uniform interface

“Uniform interface” refers to a standard interface between the client and the
resources provided by the application. This **does not mean** that resources
(in our case, model instances) are easily discoverable and set up in the exact
same way at all times. All that this means is that the interface must adhere
to _A_ standard.

That interface standard is described by four constraints:

  * A uniform identifier (i.e. URIs) for resources
  * Manipulation of resources through the representations provided by URIs and HTTP verbs
  * Self-descriptive messages that depict how you may interact with the app in general and the resource in particular
  * Hypermedia as the Engine of Application State (a.k.a. HATEOAS)

That last one is a fancy way of saying that you can use links and URI
templates (e.g. /images/photos/<photoid> instead of just /images/photos/1) to
dictate the state of the application.

#### Layered System Architecture

Similar to how we’ve been using Nginx as the intermediary between the Internet
at large and our tender little Django apps, a proper REST API restricts any
layer between the client and server to only be aware of what it’s immediately
interacting with. Our clients have no idea that they’re interacting with a
Django app serving on localhost port 8080 because Nginx sits between them.
Similarly, our Django apps have no idea that the web requests are coming from
a Chrome/Firefox/Safari browser because it only sees the requests as they are
handed out by the Nginx proxy server.

If the Client we’re using is built on ancient technology, then our layered
system can have mechanisms in place that will serve a response that it can
handle. Similarly, our layered system can provide requests that our Server can
handle, depending on the requirements of that server.

Similarly, the Client will never know which machine it’s getting a response
from when we’re working with a load-balanced network of computers. The load-
balancer is the intermediary that tries to spread work across a number of
computers/processors such that the work can be adequately handled. It doesn’t
matter which worker does handle it though, all that matters is a response is
sent back.

While this constraint on a REST API does invite more server overhead, it’s
mitigated by other advantages. Previously we spoke about cacheing. The
intermediaries between the client and server can share a cache across a
distributed network. The intermediaries can also serve as security gateways,
inspecting requests and responses to ensure that appropriate messages get
passed to where they need to go, and inappropriate ones get blocked or
rerouted elsewhere.

#### Code on Demand

Typically the resources that we request are representations of the objects
that make our app work. These come back to the client in a response as
rendered HTML, XML, or JSON. However, it can be the case that a resource is
returned to a client without the means or ability to process that resource’s
information. In this circumstance, a REST API can return code. Hence, code on
demand.

This allows for the back-end to add to or extend features of the deployed
client. It still wouldn’t manage client state, it would simply extend
functionality. It can, however, increase server performance by offloading work
to the client side.

The catch here is that the client needs to trust that the executable code the
server sends back is legitimate and should be trusted. This isn’t always
applicable, so this last constraint on a REST API is left optional.

## Wrap Up

You’ve practiced your way through the Django REST Framework tutorial, and now
you have some information as to “why”. This is, of course, not all of it but
enough to get you started. Continue work on your existing Django Imager and
add a REST API to standardize it, adding more of an ability to interact with
any front end.

