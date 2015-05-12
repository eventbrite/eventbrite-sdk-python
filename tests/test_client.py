#!/usr/bin/env python
# -*- coding: utf-8 -*-

from platform import platform

from eventbrite import __version__
from eventbrite.client import Eventbrite


def test_headers():
    eventbrite = Eventbrite('12345')
    expected_headers = {
        u'content-type': u'application/json',
        u'Authorization': u'Bearer 12345',
        u'User-Agent': "eventbrite-python-sdk {version} ({system})".format(
            version=__version__,
            system=platform(),)
    }
    assert eventbrite.headers == expected_headers
