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


    def api(self, method, path, data, expansions=()):
        method = method.strip().lower()
        if method not in self.allowed_methods:
            msg = "The '{0}' method is not accepted by the Eventbrite client.".format(
                method
            )
            raise IllegalHttpMethod(msg)
        method = getattr(self, method)
        path = format_path(path)
        return method(path, data)


    def get(self, path, data, expansions=()):
        response = requests.get(path, headers=self.headers, params=data)
        return Payload.create(response)


    def post(self, path, data, expansions=()):
        response = requests.post(path, headers=self.headers, data=data)
        return Payload.create(response)


    def delete(self, path, data, expansions=()):
        response = requests.delete(path, headers=self.headers, data=data)
        return Payload.create(response)
