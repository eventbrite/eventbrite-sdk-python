===============================
eventbrite-sdk-python
===============================

.. image:: https://badge.fury.io/py/eventbrite.png
    :target: http://badge.fury.io/py/eventbrite

.. image:: https://travis-ci.org/pydanny/eventbrite.png?branch=master
        :target: https://travis-ci.org/pydanny/eventbrite

.. image:: https://pypip.in/d/eventbrite/badge.png
        :target: https://pypi.python.org/pypi/eventbrite


Official Eventbrite SDK for Python

* Free software: BSD license
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