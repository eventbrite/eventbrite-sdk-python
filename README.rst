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

The Eventbrite Python SDK makes it trivial to interact with the Eventbrite API:

.. code-block:: python

    >>> from eventbrite import Eventbrite
    >>> eventbrite = Eventbrite('my-oauth-token')
    >>> user = eventbrite.get_user()  # Not passing an argument returns yourself
    >>> user['id']
    1234567890
    >>> user['name']
    Daniel Roy Greenfeld

You can also specify API endpoints manually:

.. code-block:: python

    >>> user = eventbrite.get('/users/me')
    >>> user['id']
    1234567890
    >>> user['name']
    Daniel Roy Greenfeld


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
