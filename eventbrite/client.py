# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .compat import string_type
from .decorators import objectify
from .models import Payload
from .exceptions import IllegalHttpMethod
from .utils import format_path
import _version

class Eventbrite(object):

    allowed_methods = ['post', 'get', 'delete']

    def __init__(self, oauth_token):
        self.oauth_token = oauth_token

    @property
    def headers(self):
        return {
            "agent": "eventbrite-python-sdk {version}".format(version=_version.__version__),
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
        return method(path, data)

    def get(self, path, data=None, expansions=()):
        path = format_path(path)
        response = requests.get(path, headers=self.headers, params=data or {})
        return Payload.create(response)

    def post(self, path, data=None, expansions=()):
        path = format_path(path)
        response = requests.post(path, headers=self.headers, data=data or {})
        return Payload.create(response)

    def delete(self, path, data=None, expansions=()):
        path = format_path(path)
        response = requests.delete(path, headers=self.headers, data=data or {})
        return Payload.create(response)

    ############################
    #
    # Access methods
    #
    ############################

    @objectify
    def get_user(self, user_id=None):
        """
        Returns a user for the specified user as user.

        users/:id/

        :param int/str user_id: (optional) The id assigned to a user

        """
        if user_id:
            return self.get('/users/{0}/'.format(user_id))
        return self.get('/users/me/')

    def get_user_orders(self, user_id=None, changed_since=None):
        """
        Returns a paginated response of orders, under the key orders, of all
        orders the user has placed (i.e. where the user was the person buying
        the tickets).

        users/:id/orders/

        :param int/str user_id: (optional) The id assigned to a user. Leave empty to get current user.
        :param datetime changed_since: (optional) Only return attendees changed on or after the time given

        .. note:: A datetime represented as a string in ISO8601 combined date and time format, always in UTC.
        """
        if user_id:
            url = '/users/{0}/'.format(user_id)
        else:
            url = '/users/me/'

        data = {}
        if changed_since:
            data['changed_since'] = changed_since
        return self.get(url, data=data)

    def get_user_owned_events(self, user_id=None, status=None, order_by=None):
        pass
