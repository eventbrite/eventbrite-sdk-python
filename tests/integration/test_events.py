#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta, datetime
import os
import json

from eventbrite import Eventbrite
from eventbrite.utils import EVENTBRITE_API_URL

from ..base import unittest

try:
    OAUTH_TOKEN = os.environ[u'EVENTBRITE_OAUTH_TOKEN']
    skip_integration_tests = False
except KeyError:
    skip_integration_tests = True

try:
    USER_ID = os.environ[u'EVENTBRITE_USER_ID']
    skip_user_id_tests = False
except KeyError:
    skip_user_id_tests = True


class TestEvents(unittest.TestCase):

    def setUp(self):
        self.eventbrite = Eventbrite(OAUTH_TOKEN)

    @unittest.skipIf(condition=skip_user_id_tests, reason='Needs a USER_ID')
    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_post_event(self):

        event_name = 'client_test_{0}'.format(datetime.now())

        event_data = {
          'event.name': {
            'html': event_name,
          },
          'event.start': {
            'utc': '2015-03-07T20:00:00Z',
            'timezone': 'America/Los_Angeles',
          },
          'event.end': {
            'utc': '2015-03-07T23:00:00Z',
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
        event = self.eventbrite.post('/events/', data=event_data)
        self.assertEqual(event_name, event['name']['text'])
        self.assertEqual(event_name, event['name']['html'])
        # Just for access to see the event, not full authentication
        self.assertEqual(event['password'], "test")

    @unittest.skipIf(condition=skip_user_id_tests, reason='Needs a USER_ID')
    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_search_events(self):
        data = {
          'location.latitude':'40.4313684',
          'start_date.keyword':'today',
          'location.longitude':'-79.9805005',
          'location.within':'10km'
        }
        events = self.eventbrite.event_search(**data)
        self.assertLess(events['pagination'][u'object_count'], 1000)

if __name__ == '__main__':
    unittest.main()
