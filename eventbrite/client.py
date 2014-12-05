# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from .compat import json, string_type
from .decorators import objectify
from .exceptions import IllegalHttpMethod
from .utils import format_path
from . import _version


class Eventbrite(object):

    allowed_methods = ['post', 'get', 'delete']

    def __init__(self, oauth_token):
        self.oauth_token = oauth_token

    @property
    def headers(self):
        return {
            "agent": "eventbrite-python-sdk {version}".format(
                version=_version.__version__
                ),
            "Authorization": "Bearer {0}".format(self.oauth_token),
            "content-type": "application/json"
        }

    def api(self, method, path, data, expansions=()):
        method = method.strip().lower()
        if method not in self.allowed_methods:
            msg = "The '{0}' method is not accepted by the Eventbrite " \
                "client.".format(method)
            raise IllegalHttpMethod(msg)
        method = getattr(self, method)
        return method(path, data)

    @objectify
    def get(self, path, data=None, expansions=()):
        path = format_path(path)
        return requests.get(path, headers=self.headers, params=data or {})

    @objectify
    def post(self, path, data=None, expansions=()):
        path = format_path(path)
        return requests.post(path, headers=self.headers, data=data or {})

    @objectify
    def delete(self, path, data=None, expansions=()):
        path = format_path(path)
        return requests.delete(path, headers=self.headers, data=data or {})

    ############################
    #
    # Access methods
    #
    ############################

    def get_user(self, user_id=None):
        """
        Returns a user for the specified user as user.

        GET users/:id/

        :param int user_id: (optional) The id assigned to a user

        """
        if user_id:
            return self.get('/users/{0}/'.format(user_id))
        return self.get('/users/me/')

    def get_user_orders(self, user_id=None, changed_since=None):
        """
        Returns a paginated response of orders, under the key orders, of all
        orders the user has placed (i.e. where the user was the person buying
        the tickets).

        GET users/:id/orders/

        :param int user_id: (optional) The id assigned to a user. Leave empty to get current user.
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

    def get_order(self, order_id):
        """
        GET /orders/:id/
        """
        return self.get("/orders/{0}/".format(order_id))

    def get_event(self, event_id):
        """
        GET /events/:id/
        """
        return self.get("/events/{0}/".format(event_id))

    def get_event_attendees(self, event_id, status=None, changed_since=None):
        """
        Returns a paginated response with a key of attendees, containing a list of attendee.

        GET /events/:id/attendees/
        """
        data = {}
        if status:  # TODO - check the types of valid status
            data['status'] = status
        if changed_since:
            data['changed_since'] = changed_since
        return self.get("/events/{0}/attendees/".format(event_id), data=data)

    def get_event_attendee_by_id(self, event_id, attendee_id):
        """
        GET /events/:id/attendees/:id/
        """
        return self.get("/events/{0}/attendees/{1}/".format(event_id, attendee_id))

    def get_event_ticket_classes(self, event_id):
        """
        Returns a paginated response with a key of ticket_classes, containing a list of ticket_class.

        GET /events/:id/ticket_classes/
        """
        return self.get("/events/{0}/attendees/".format(event_id))

    def get_event_ticket_class_by_id(self, event_id, ticket_class_id):
        """
        GET /events/:id/ticket_classes/:id/
        """
        return self.get("/events/{0}/attendees/{1}/".format(event_id, ticket_class_id))

    def webhook_to_object(self, webhook):
        """
        Converts JSON sent by an Eventbrite Webhook to the appropriate Eventbrite object.

        # TODO - Be able to handle Django and Flask request objects
        """
        if isinstance(webhook, string_type):
            # If still JSON, convert to a Python dict
            webhook = json.dumps(webhook)
        payload = self.get(webhook['api_url'])

        return payload
