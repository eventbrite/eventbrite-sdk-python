# -*- coding: utf-8 -*-
from os import environ
import os.path
import re

from .compat import (
    string_type,
    json,
    urlparse,
    urljoin
)
from .exceptions import (
    InvalidResourcePath,
    UnknownEndpoint,
    UnsupportedEndpoint,
)

EVENTBRITE_API_URL = environ.get('EVENTBRITE_API_URL', 'https://www.eventbriteapi.com/v3/')
EVENTBRITE_API_PATH = urlparse(EVENTBRITE_API_URL).path

URL_MAP_FILE = os.path.join(os.path.dirname(__file__), "apiv3_url_mapping.json")


def get_mapping(_compiled_mapping=[]):
    if _compiled_mapping:
        return _compiled_mapping
    try:
        mapping = json.load(open(URL_MAP_FILE))
        for endpoint in mapping:
            endpoint["url_regexp"] = re.compile(endpoint["url_regexp"])
        _compiled_mapping = mapping
        return _compiled_mapping
    except Exception:
        raise  # TODO: do we handle it here?


def reverse(path_or_url, only_serialized=False):
    """Look up data types returned by API endpoint for specific url/path
    """
    parsed_url = urlparse(path_or_url)
    path = parsed_url.path
    if not path.startswith(EVENTBRITE_API_PATH):
        error_msg = "The path argument must be a string that begins with '{0}'".format(EVENTBRITE_API_PATH)
        raise InvalidResourcePath(error_msg)
    stripped_path = path[len(EVENTBRITE_API_PATH):]  # cutting of the common prefix
    mapping = get_mapping()
    for endpoint in mapping:
        matches = re.match(endpoint["url_regexp"], stripped_path)
        if matches:
            if endpoint["data_type"] == "UNKNOWN":
                raise UnsupportedEndpoint(path)
            if only_serialized and endpoint["data_type"] != "serialized":
                raise UnsupportedEndpoint(path)
            return endpoint
    raise UnknownEndpoint(path)


def format_path(path, eventbrite_api_url=EVENTBRITE_API_URL):
    error_msg = "The path argument must be a string that begins with '/'"
    if not isinstance(path, string_type):
        raise InvalidResourcePath(error_msg)
    # Probably a webhook path
    if path.startswith(eventbrite_api_url):
        return path

    # Using the HTTP shortcut
    if path.startswith("/"):
        return urljoin(eventbrite_api_url, path.lstrip('/'))
    raise InvalidResourcePath(error_msg)


def construct_namespaced_dict(namespace, unfiltered_dict):
    result_dict = {namespace: {}}
    for key, value in unfiltered_dict.items():
        if key.startswith(namespace):
            result_dict[namespace][key[len(namespace)+1:]] = value
    return result_dict


def get_webhook_from_request(request):
    if hasattr(request, "get_json"):
        return request.get_json()

    return request
