# -*- coding: utf-8 -*-
import pprint


class Payload(dict):
    """The object returned from the low-level client calls:

        * .api()
        * .get()
        * .post()
        * .delete()
    """

    @classmethod
    def create(cls, response):
        payload = cls(response.json())
        payload.url = response.url
        payload.ok = response.ok
        payload.elapsed = response.elapsed
        payload.headers = response.headers
        payload.reason = response.reason
        payload.status_code = response.status_code
        return payload

    @property
    def pretty(self):
        return pprint.pformat(self)


    def objectify(self):
        """Returns an EventbriteObject representation of the Payload"""
        pass


class EventbriteObject(Payload):

    list = None
    pagination = None
    payload = {}
    type = ""
    id = pk = None

    @classmethod
    def create_from_payload(cls, payload):
        evbobject = cls(payload)
        evbobject.url = payload.url
        evbobject.ok = payload.ok
        evbobject.elapsed = payload.elapsed
        evbobject.headers = payload.headers
        evbobject.reason = payload.reason
        evbobject.status_code = payload.status_code
        evbobject.pagination = evbobject.list = payload.get('pagination')
        evbobject.pk = evbobject.id = payload.get('id')
        return evbobject
