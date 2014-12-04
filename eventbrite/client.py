# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .exceptions import IllegalHttpMethod
from .utils import format_path

__all__ = ['EVENTBRITE_API_URL', 'IllegalHttpMethod', 'Eventbrite']

EVENTBRITE_API_URL = "https://www.eventbriteapi.com/v3"


class Eventbrite(object):

    allowed_methods = ['post', 'get', 'delete']

    def __init__(self, oauth_token):
        self.oauth_token = oauth_token


    @property
    def headers(self):
        return {
            "agent": "eventbrite-python-sdk 0.1.0",
            "Authorization": "Bearer {0}".format(self.oauth_token),
            "content-type": "application/json"
        }


    def api(self, method, path, expansions=(), **kwargs):
        method = method.strip().lower()
        if method not in self.allowed_methods:
            msg = "The '{0}' method is not accepted by the Eventbrite client.".format(
                method
            )
            raise IllegalHttpMethod(msg)
        method = getattr(self, method)
        method(path, **params)


    def get(self, path, expansions=(), **kwargs):
        path = format_path(path)
        return requests.get(path, headers=self.headers, params=kwargs)


    def post(self, path, expansions=(), **kwargs):
        path = format_path(path)
        return requests.post(path, headers=self.headers, data=kwargs)


    def delete(self, path, expansions=(), **kwargs):
        path = format_path(path)
        return requests.delete(path, headers=self.headers, data=kwargs)
