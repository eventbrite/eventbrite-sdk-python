# -*- coding: utf-8 -*-
class Payload(dict):

    @classmethod
    def create(cls, url, payload):
        obj = cls(payload)
        obj.url = url
        return obj