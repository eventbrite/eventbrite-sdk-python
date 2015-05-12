#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta

from eventbrite.compat import PY3
from eventbrite.models import EventbriteObject

from requests.structures import CaseInsensitiveDict

from .base import unittest, mock


class TestEventbriteObject(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.eventbriteapi.com/v3/users/me/"
        self.response = mock.Mock()
        self.response.json = lambda: {u'id': u'1234567890', u'first_name': u'Daniel', u'last_name': u'Greenfeld', u'emails': [{u'verified': True, u'email': u'danny@eventbrite.com', u'primary': True}], u'name': u'Daniel Greenfeld'}  # noqa
        self.response.url = self.url
        self.response.ok = True
        self.response.elapsed = timedelta(5)
        self.response.headers = CaseInsensitiveDict()
        self.response.reason = u"OK"
        self.response.status_code = 200

        self.evbobject = EventbriteObject.create(self.response)

    def test_create_from_payload(self):

        evbobject = self.evbobject

        self.assertEqual(
            sorted([u'id', u'first_name', u'last_name', u'emails', u'name']),
            sorted(evbobject.keys())
        )

        self.assertTrue(evbobject.ok)
        self.assertEqual(
            self.url,
            evbobject.resource_uri
        )
        self.assertTrue(isinstance(evbobject.elapsed, timedelta))
        self.assertTrue(isinstance(evbobject.headers, CaseInsensitiveDict))

    @unittest.skipIf(condition=PY3, reason='Python 3 appears to return stdout')
    def test_pretty(self):

        self.assertEqual(
            self.evbobject.pretty,
            "{u'emails': [{u'email': u'danny@eventbrite.com',\n              u'primary': True,\n              u'verified': True}],\n u'first_name': u'Daniel',\n u'id': u'1234567890',\n u'last_name': u'Greenfeld',\n u'name': u'Daniel Greenfeld'}"  # noqa
        )

if __name__ == '__main__':
    unittest.main()
