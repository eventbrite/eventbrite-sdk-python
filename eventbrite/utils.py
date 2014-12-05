# -*- coding: utf-8 -*-
from urlparse import urljoin, urlparse
import os.path
import re

from .compat import (
    string_type,
    json,
)
from .exceptions import InvalidResourcePath

EVENTBRITE_API_URL = 'https://www.eventbriteapi.com/v3/'
EVENTBRITE_API_PATH = urlparse(EVENTBRITE_API_URL).path

URL_MAP_FILE = os.path.join(os.path.realpath(__file__), "apiv3_url_mapping.json")

def get_mapping(_compiled_mapping=[]):
    if _compiled_mapping:
        return _compiled_mapping
    try:
        mapping = json.load(os.open(URL_MAP_FILE))
        for endpoint in mapping:
            endpoint["url_regex"] = re.compile(endpoint["url_regex"])
        _compiled_mapping = mapping
        return _compiled_mapping
    except Exception:
        raise  # TODO: do we handle it here?


def reverse(path):
    if not path.startswith(EVENTBRITE_API_PATH):
        error_msg = "The path argument must be a string that begins with '{0}'".format(EVENTBRITE_API_PATH)
        raise InvalidResourcePath(error_msg)
    path = path[4:]  # cutting of the common prefix
    mapping = get_mapping()
    for endpoint in mapping:
        matches = re.match(endpoint["url_regex"], path)
        if matches:
            return endpoint


def format_path(path):
    error_msg = "The path argument must be a string that begins with '/'"
    if not isinstance(path, string_type):
        raise InvalidResourcePath(error_msg)
<<<<<<< HEAD
    # Probably a webhook path
    if path.startswith(EVENTBRITE_API_URL):
        return path

    # Using the HTTP shortcut
    if path,startswith("/"):
        return "{0}{1}".format(EVENTBRITE_API_URL, path)

    raise InvalidResourcePath(error_msg)
=======
    if path[0] != "/" and not path.startswith(EVENTBRITE_API_URL):
        raise InvalidResourcePath(error_msg)
    return urljoin(EVENTBRITE_API_URL, path)
>>>>>>> implementing reverse magic
