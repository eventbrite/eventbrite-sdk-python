# -*- coding: utf-8 -*-
import pprint


class EventbriteObject(dict):

    list = None
    pagination = None
    type = ""
    id = None
    pk = None

    @classmethod
    def create(cls, response):
        data = response.json()
        evbobject = cls(data)
        evbobject.url = response.url
        evbobject.ok = response.ok
        evbobject.elapsed = response.elapsed
        evbobject.headers = response.headers
        evbobject.reason = response.reason
        evbobject.status_code = response.status_code
        evbobject.pagination = evbobject.list = data.get('pagination')
        evbobject.pk = evbobject.id = data.get('id')
        evbobject.type = ""
        return evbobject

    @property
    def pretty(self):
        return pprint.pformat(self)
