#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta, datetime
import os

from requests.structures import CaseInsensitiveDict

from eventbrite import Eventbrite
from eventbrite.models import EventbriteObject
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


class TestClient(unittest.TestCase):

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_api_get(self):
        eventbrite = Eventbrite(OAUTH_TOKEN)

        payload = eventbrite.api("get", "/users/me/", {})

        self.assertEqual(
            sorted([u'id', u'first_name', u'last_name', u'emails', u'name']),
            sorted(payload.keys())
        )

        self.assertEqual(
            payload.resource_uri,
            EVENTBRITE_API_URL + 'users/me/'
        )

        self.assertTrue(payload.ok)
        self.assertTrue(isinstance(payload.elapsed, timedelta))
        self.assertTrue(isinstance(payload.headers, CaseInsensitiveDict))

        self.assertFalse(
            'content-type' in payload.request.headers
        )

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_api_post(self):
        pass  # TODO

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_api_delete(self):
        pass  # TODO


class TestClientAccessMethods(unittest.TestCase):

    def setUp(self):
        self.eventbrite = Eventbrite(OAUTH_TOKEN)

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_get_user_me(self):
        evbobject = self.eventbrite.get_user()

        # Did we get an EventbriteObject?
        self.assertTrue(isinstance(evbobject, EventbriteObject))

        # check attributes
        for attribute in ['id', 'pk', 'type', 'is_paginated', 'is_list', 'status_code']:
            self.assertTrue(attribute in evbobject.__dict__.keys())

        # check that an ID exists
        self.assertTrue(evbobject.get('id'))

    @unittest.skipIf(condition=skip_user_id_tests, reason='Needs a USER_ID')
    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_get_user(self):
        evbobject = self.eventbrite.get_user(USER_ID)

        # Did we get an EventbriteObject?
        self.assertTrue(isinstance(evbobject, EventbriteObject))

        # check attributes
        for attribute in ['id', 'pk', 'type', 'is_paginated', 'is_list', 'status_code']:
            self.assertTrue(attribute in evbobject.__dict__.keys())

        # check that the ID's match
        self.assertEqual(evbobject.get('id'), USER_ID)

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_webhook_no_internet(self):
        webhook = {
            "api_url": EVENTBRITE_API_URL + 'users/me/',
            "config": {
                "endpoint_url": "https://myawesomeapp.com/webhook",
                "insecure_ssl": "0"
            }
        }
        evbobject = self.eventbrite.webhook_to_object(webhook)
        self.assertTrue('id' in evbobject)
