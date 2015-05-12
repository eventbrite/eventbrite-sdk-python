#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_eventbrite
----------------------------------

Tests for `eventbrite` module.
"""
from eventbrite.exceptions import InvalidResourcePath
from eventbrite.utils import (
    format_path,
    get_webhook_from_request,
    EVENTBRITE_API_URL
)

from .base import unittest, mock


class TestFormatPath(unittest.TestCase):

    def test_invalid_type(self):

        # Check if a string is passed in
        with self.assertRaises(InvalidResourcePath):
            format_path(5)

        with self.assertRaises(InvalidResourcePath):
            format_path("https://www.eventbrite.com")

        with self.assertRaises(InvalidResourcePath):
            format_path("http://www.eventbriteapi.com/v3/users/me/")

        with self.assertRaises(InvalidResourcePath):
            format_path("users/me/")

    def test_formatted_path(self):
        path = format_path('/users/me')
        self.assertEqual(path, EVENTBRITE_API_URL + 'users/me')

    def test_get_webhook_request(self):
        # Construct our mock Flask request
        request = mock.Mock()
        data = {
            "api_url": "https://www.eventbriteapi.com/v3/users/me/",
            "config": {
                "endpoint_url": "https://eb-demo-3.herokuapp.com/webhook",
                "insecure_ssl": "0"
            }
        }
        request.get_json = lambda: data

        # Test to see if the data can be fetched correctly
        request_data = get_webhook_from_request(request)
        self.assertEqual(data, request_data)


if __name__ == '__main__':
    unittest.main()
