# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .models import Payload
from .exceptions import IllegalHttpMethod
from .utils import format_path


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
        path = format_path(path)
        method(path, **params)


    def get(self, path, expansions=(), **kwargs):
        response = requests.get(path, headers=self.headers, params=kwargs)
        return Payload(response)


    def post(self, path, expansions=(), **kwargs):
        response = requests.post(path, headers=self.headers, data=kwargs)
        return Payload(response)


    def delete(self, path, expansions=(), **kwargs):
        response = requests.delete(path, headers=self.headers, data=kwargs)
        return Payload(response)
