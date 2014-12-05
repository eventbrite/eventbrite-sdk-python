========
Usage
========

To use eventbrite-sdk-python in a project:

.. sourcecode:: python

    from eventbrite import Eventbrite
    eventbrite = Eventbrite('my-oauth-token')


Example: Get User Info
======================

The following code gets our user object and prints our `id` and `name`.

.. sourcecode:: python

    user = eventbrite.get_user()  # Not passing an argument returns yourself
    print(user['id'])
    print(user['name'])

This is what gets printed out:

::

    1234567890
    Daniel Roy Greenfeld


Example: Pretty print an object
===============================

Eventbrite objects are dictionaries with extra attributes. Our favorite is
`pretty`, which formats their data more legibly:

.. sourcecode:: python

    >>> user = eventbrite.get_user()  # Not passing an argument returns yourself
    >>> print(user.pretty)
    {u'emails': [{u'email': u'danny@eventbrite.com',
                  u'primary': True,
                  u'verified': True}],
     u'first_name': u'Daniel',
     u'id': u'1234567890',
     u'last_name': u'Greenfeld',
     u'name': u'Daniel Greenfeld'}

