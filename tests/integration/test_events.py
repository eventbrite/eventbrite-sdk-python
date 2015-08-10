#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta
from time import strftime
import os

from eventbrite import Eventbrite

from ..base import unittest

OAUTH_TOKEN = os.environ.get('EVENTBRITE_OAUTH_TOKEN', '')
if OAUTH_TOKEN:
    skip_integration_tests = False
else:
    skip_integration_tests = True

try:
    USER_ID = os.environ[u'EVENTBRITE_USER_ID']
    skip_user_id_tests = False
except KeyError:
    skip_user_id_tests = True

EB_ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class TestEvents(unittest.TestCase):

    def setUp(self):
        self.eventbrite = Eventbrite(OAUTH_TOKEN)

    @unittest.skipIf(condition=skip_user_id_tests, reason='Needs a USER_ID')
    @unittest.skipIf(
        condition=skip_integration_tests,
        reason='Needs an OAUTH_TOKEN')
    def test_post_event(self):
        event_name = 'client_test_{0}'.format(datetime.now())
        event_data = self._get_event_data(event_name)
        event = self.eventbrite.post_event(event_data)
        self.assertEqual(event_name, event['name']['text'])
        self.assertEqual(event_name, event['name']['html'])
        # Just for access to see the event, not full authentication
        self.assertEqual(event['password'], "test")

    @unittest.skipIf(condition=skip_user_id_tests, reason='Needs a USER_ID')
    @unittest.skipIf(
        condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_search_events(self):
        data = {
            'location.latitude': '40.4313684',
            'start_date.keyword': 'today',
            'location.longitude': '-79.9805005',
            'location.within': '10km'
        }
        events = self.eventbrite.event_search(**data)
        self.assertLess(events['pagination'][u'object_count'], 1000)

    @unittest.skipIf(
        condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_publish_unpublish_event(self):

        """ First, creat a draft event """
        event_data = self._get_event_data()
        event = self.eventbrite.post_event(event_data)
        self.assertTrue(event.ok,
                        msg=event.get('error_description', None))

        """ Next, create a ticket class for the event, because an event
            can't be published without one """
        ticket_data = self._get_ticket_data()
        response = self.eventbrite.post_event_ticket_class(event['id'],
                                                           data=ticket_data)

        """Finally, try to publish the event"""
        response = self.eventbrite.publish_event(event['id'])
        self.assertTrue(response.ok,
                        msg=response.get('error_description', None))

        """Now try to unpublish the event"""
        response = self.eventbrite.unpublish_event(event['id'])
        self.assertTrue(response.ok,
                        msg=response.get('error_description', None))

    @unittest.skipIf(
        condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_create_ticket_class(self):

        event_data = self._get_event_data()
        event = self.eventbrite.post_event(event_data)

        ticket_data = self._get_ticket_data()
        response = self.eventbrite.post_event_ticket_class(event['id'],
                                                           data=ticket_data)
        self.assertTrue(response.ok,
                        msg=response.get('error_description', None))

    def _get_ticket_data(self):

        return {
            'ticket_class.name': 'client_test_ticket_{0}'.format(datetime.now()),
            'ticket_class.description': 'Python API Client testing',
            'ticket_class.quantity_total': 100,
            'ticket_class.cost': 'USD,4500'
        }

    def _get_event_data(self, event_name='client_test_{0}'.format(datetime.now())):
        """ Returns a dictionary representing a valid event """

        # if not event_name:
        #     event_name = 'client_test_{0}'.format(datetime.now())

        return {
            'event.name': {
                'html': event_name,
            },
            'event.start': {
                'utc': (datetime.now() + timedelta(days=1)).strftime(EB_ISO_FORMAT),
                'timezone': 'America/Los_Angeles',
            },
            'event.end': {
                'utc': (datetime.now() + timedelta(days=1,hours=1)).strftime(EB_ISO_FORMAT),
                'timezone': 'America/Los_Angeles',
            },
            'event.currency': 'USD',
            'event.online_event': True,
            'event.listed': False,
            'event.category_id': '110',
            'event.format_id': '5',
            'event.password': "test",
            'event.capacity': 10,
        }


if __name__ == '__main__':
    unittest.main()
