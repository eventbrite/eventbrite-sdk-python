Cookbook
=========

Get a List of My Draft/Unpublished Events
-----------------------------------------

.. code-block:: python

    from eventbrite import Eventbrite
    eventbrite = Eventbrite(MY_OAUTH_TOKEN)

    # Get my own User ID
    my_id = eventbrite.get_user()['id']

    # Get a raw list of events (includes pagination details)
    events = eventbrite.event_search(**{'user.id': my_id})

    # List the events in draft status
    [x for x in events['events'] if x['status'] == 'draft']
