===============================
eventbrite-sdk-python
===============================

.. image:: https://badge.fury.io/py/eventbrite.png
    :target: http://badge.fury.io/py/eventbrite

.. image:: https://travis-ci.org/eventbrite/eventbrite-sdk-python.svg?branch=master
        :target: https://travis-ci.org/eventbrite/eventbrite-sdk-python

.. image:: https://pypip.in/d/eventbrite/badge.png
        :target: https://pypi.python.org/pypi/eventbrite


Official Eventbrite SDK for Python

* Free software: Apache 2 license
* Documentation: https://eventbrite.readthedocs.org.

Usage
--------

At the most basic level, the Eventbrite API is a wrapper around the requests_
library::

    >>> from eventbrite import Eventbrite
    >>> eventbrite = Eventbrite('my-oauth-token')
    >>> payload = eventbrite.get('/users/me')
    {u'emails': [{u'email': u'danny@eventbrite.com',
                  u'primary': True,
                  u'verified': True}],
     u'first_name': u'Daniel',
     u'id': u'103945044409',
     u'last_name': u'Greenfeld',
     u'name': u'Daniel Greenfeld'}


.. _requests: https://pypi.python.org/pypi/requests


TODOS
--------

Abstract the HTTP calls so they can work with:

* requests
* Google's HTTP client
* Tornado
* plain urllib/urllib2 (ugh)

Calling different HTTP libraries::

    Eventbrite(OAUTH_TOKEN, "requests")
    Eventbrite(OAUTH_TOKEN, "google")
    Eventbrite(OAUTH_TOKEN, "tornado")
    Eventbrite(OAUTH_TOKEN, "native")