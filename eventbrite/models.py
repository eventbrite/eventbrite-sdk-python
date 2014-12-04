# -*- coding: utf-8 -*-
class Payload(dict):

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