#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import timedelta
import os

from requests.structures import CaseInsensitiveDict

from eventbrite import Eventbrite

from ..base import unittest

try:
    oauth_token = os.environ.get(u'OAUTH_TOKEN')
    skip_integration_tests = False
except KeyError:
    skip_integration_tests = True


class TestClient(unittest.TestCase):

    @unittest.skipIf(condition=skip_integration_tests, reason='Needs an OAUTH_TOKEN')
    def test_user_me(self):
        eventbrite = Eventbrite(oauth_token)

        payload = eventbrite.api("get", "/users/me/", {})

        self.assertEqual(
            [u'id', u'first_name', u'last_name', u'emails', u'name'],
            payload.keys()
        )

        self.assertEqual(
            payload.url,
            "https://www.eventbriteapi.com/v3/users/me/"
        )

        self.assertTrue(payload.ok)
        self.assertTrue(isinstance(payload.elapsed, timedelta))
        self.assertTrue(isinstance(payload.headers, CaseInsensitiveDict))


if __name__ == '__main__':
    unittest.main()
