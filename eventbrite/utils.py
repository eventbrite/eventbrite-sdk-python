# -*- coding: utf-8 -*-

from .exceptions import InvalidResourcePath

EVENTBRITE_API_URL = "https://www.eventbriteapi.com/v3"


def reverse(path):
    """
        Determine the Eventbrite API v3 object type based on a path.
        Throw an InvalidResourcePath exception if it fails

        TODO
    """
    return ""


def format_path(path):
    error_msg = "The path argument must be a string that begins with '/'"
    if not isinstance(path, basestring):
        raise InvalidResourcePath(error_msg)
    if path[0] != "/":
        raise InvalidResourcePath(error_msg)
    return "{0}{1}".format(EVENTBRITE_API_URL, path)