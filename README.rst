===============================
eventbrite-sdk-python
===============================

.. image:: https://badge.fury.io/py/eventbrite.png
    :target: http://badge.fury.io/py/eventbrite

.. image:: https://travis-ci.org/eventbrite/eventbrite-sdk-python.svg?branch=master
        :target: https://travis-ci.org/eventbrite/eventbrite-sdk-python

.. image:: https://pypip.in/d/eventbrite/badge.png
        :target: https://pypi.python.org/pypi/eventbrite


Official Eventbrite_ SDK for Python

* Free software: Apache 2 license
* Documentation: https://eventbrite.readthedocs.org.

Usage
--------

The  Eventbrite python SDK makes it trivial to interact with the Eventbrite API:

    >>> from eventbrite import Eventbrite
    >>> eventbrite = Eventbrite('my-oauth-token')
    >>> user = eventbrite.get_user()  # Not passing an argument returns yourself
    >>> print(user.pretty)
    {u'emails': [{u'email': u'danny@eventbrite.com',
                  u'primary': True,
                  u'verified': True}],
     u'first_name': u'Daniel',
     u'id': u'1234567890',
     u'last_name': u'Greenfeld',
     u'name': u'Daniel Greenfeld'}

At the most lowest level, the Eventbrite python SDK is a wrapper around the requests_
library::

    >>> user = eventbrite.get('/users/me')
    >>> print(user.pretty)
    {u'emails': [{u'email': u'danny@eventbrite.com',
                  u'primary': True,
                  u'verified': True}],
     u'first_name': u'Daniel',
     u'id': u'1234567890',
     u'last_name': u'Greenfeld',
     u'name': u'Daniel Greenfeld'}


.. _requests: https://pypi.python.org/pypi/requests
.. _Eventbrite: https://www.eventbrite.com


TODOS
--------

Abstract the HTTP calls so they can work with all of the below:

* requests
* Google's HTTP client
* Tornado

Calling different HTTP libraries::

    Eventbrite(OAUTH_TOKEN, "requests")
    Eventbrite(OAUTH_TOKEN, "google")
    Eventbrite(OAUTH_TOKEN, "tornado")
