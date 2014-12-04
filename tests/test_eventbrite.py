#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_eventbrite
----------------------------------

Tests for `eventbrite` module.
"""

from eventbrite.compat import unittest, patch

from eventbrite import Eventbrite


class TestEventbriteNonHttp(unittest.TestCase):

    def setUp(self):
        self.evb = Eventbrite("1234567890")

    def test_pathify(self):
        path = "/events/{event_id}/orders/{order_id}"

        kwargs = {"event_id": 1, "order_id": 2}
        new_path = self.evb.pathify(path, **kwargs)

        self.assertEqual('/events/1/orders/2', new_path)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
