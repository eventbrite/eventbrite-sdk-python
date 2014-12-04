#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_eventbrite
----------------------------------

Tests for `eventbrite` module.
"""

from eventbrite.exceptions import InvalidResourcePath
from eventbrite.utils import format_path


from .base import unittest


class TestFormatPath(unittest.TestCase):

    def test_invalid_type(self):

        # Check if a string is passed in
        with self.assertRaises(InvalidResourcePath):
            format_path(5)

        with self.assertRaises(InvalidResourcePath):
            format_path("https://www.eventbriteapi.com/v3/users/me/")

        with self.assertRaises(InvalidResourcePath):
            format_path("http://www.eventbriteapi.com/v3/users/me/")

        with self.assertRaises(InvalidResourcePath):
            format_path("users/me/")

    def test_formatted_path(self):
        path = format_path('/users/me')

        self.assertEqual(path, "https://www.eventbriteapi.com/v3/users/me")


if __name__ == '__main__':
    unittest.main()
