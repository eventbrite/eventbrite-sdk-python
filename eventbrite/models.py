# -*- coding: utf-8 -*-
import pprint
from .utils import reverse


class EventbriteObject(dict):

    is_list = None
    pagination = None  # pagination dict w/ keys: object_count, page_number, page_size, page_count
    type = ""
    id = None
    pk = None

    @classmethod
    def create(cls, response):
        data = response.json()
        evbobject = cls(data)
        evbobject.resource_uri = response.url
        evbobject.ok = response.ok
        evbobject.elapsed = response.elapsed
        evbobject.headers = response.headers
        evbobject.reason = response.reason
        evbobject.status_code = response.status_code
        evbobject._set_from_reverse()
        evbobject._set_from_data(data)
        return evbobject

    def _set_from_reverse(self):
        api_data_type = reverse(self.resource_uri)
        # TODO: figure out what to do with enpoint, which don't have defined serializer
        # TODO: solve issue with non-standard serializes not mapping directly to defined objects
        self.type = api_data_type.get("serializer", "")
        # if it's paginated, it's a list, otherwise we don't know yet
        if api_data_type.get("response_type") == "paginated_response":
            self.is_list = True

    def _set_from_data(self, data):
        self.pk = self.id = data.get('id')
        self.pagination = data.get('pagination')

    @property
    def is_paginated(self):
        return bool(self.pagination)

    @property
    def pretty(self):
        return pprint.pformat(self)
