===============================
eventbrite-sdk-python
===============================

.. image:: https://badge.fury.io/py/eventbrite.png
    :target: http://badge.fury.io/py/eventbrite

.. image:: https://travis-ci.org/eventbrite/eventbrite-sdk-python.svg?branch=master
        :target: https://travis-ci.org/eventbrite/eventbrite-sdk-python


* Official Eventbrite_ SDK for Python
* Full Documentation: http://eventbrite-sdk-python.readthedocs.org/
* API Reference: https://developer.eventbrite.com/docs/

Installation from PyPI
----------------------

::

    $ pip install eventbrite

If you need to, you can also use `easy_install`::

    $ easy_install eventbrite

Usage
-----

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

Expansions_ can be included in a returned GET resource by simply adding the ``expand`` keyword to the calling method:

.. code-block:: python

    >>> event = eventbrite.get_event('my-event-id')
    >>> 'ticket_classes' in evbobject
    False
    >>> event = eventbrite.get_event('my-event-id', expand='ticket_classes')
    >>> 'ticket_classes' in evbobject
    True

.. _Expansions: http://www.eventbrite.com/developer/v3/reference/expansions/

Usage with Frameworks
----------------------

When using Flask, you can convert incoming webhook requests into Eventbrite
API objects using the `webhook_to_object()` method:

.. code-block:: python

    @app.route('/webhook', methods=['POST'])
    def webhook():


        # Use the API client to convert from a webhook to an API object
        api_object = eventbrite.webhook_to_object(request)

        # Process the API object
        if api_object.type == 'User':
            do_user_process(api_object)

        if api_object.type == 'Event':
            do_event_process(api_object)

        return ""

Versioning
----------

Because this client interacts with Eventbrite's third API (a.k.a. APIv3), we are tying our release numbers against it in a modified-semantic system:

* 3.x.x where '3' matches the API version. This will not change until Eventbrite releases a new API version.
* x.0.x where '0' is increased any time there is a significant change to the API that possibly breaks backwards compatibility
* x.x.1 where '1' is increased on any release that does not break backwards comptability (small, new features, enhancements, bugfixes)

.. _requests: https://pypi.python.org/pypi/requests
.. _Eventbrite: https://www.eventbrite.com

Contributing
------------

Bug reports and pull requests are welcome on GitHub at https://github.com/eventbrite/eventbrite-sdk-python.


License
-------

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
www.onchykma.wordpress.com
www.kmaonchy.wordpress.com
www.kmaonchy.blogspot.co.id
https://plus.google.com/11671425784368683945
https://twitter.com/kmaonchy?s=09
https://m.facebook.com/karya.mandiri.aluminium1
https://www.instagram.com/kma_onchy/
https://www.instagram.com/kma_onchy_com/
https://path.com/id/kmaonchy
https://kmaonchy.tumblr.com/
https://www.linkedin.com/in/karya-mandiri-aluminium-a484a4137
karya.mandiri.aluminium94@gmail.com
kma.onchy@gmail.com
suxesku@gmail.com
karyamandiri_alumunium94@yahoo.com
+6282318291238
http://os.bikinaplikasi.com/download/kmaonchycom
https://kmaonchycom.easy.co/
https://app.mailerlite.com/emails/step2_b/11216176
https://commons.m.wikimedia.org/wiki/User_talk:Kmaonchy?markasread=7484639#/editor/0
https://id.pinterest.com/kmaonchy/
https://www.amazon.in/gp/yourstore/home?ie=UTF8&ref_=nav_youraccount_switchacct
https://app.mailerlite.com/emails/step2/11216174#/edit_tab_settings
https://www.facebook.com/kmaonchy/
