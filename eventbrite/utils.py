# -*- coding: utf-8 -*-

from .utils import InvalidResourcePath

def reverse(path):
    """
        Determine the Eventbrite API v3 object type based on a path.
        Throw an InvalidResourcePath exception if it fails
    """
    return ""


def format_path(self, path):
    error_msg = "The path argument must be a string that begins with '/'"
    if not isinstance(path, basestring):
        raise TypeError(error_msg)
    if path[0] != "/":
        raise TypeError(error_msg)
    return "{0}{1}".format(EVENTBRITE_API_URL, path)