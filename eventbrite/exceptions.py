# -*- coding: utf-8 -*-

class EventbriteException(Exception):
    pass


class IllegalHttpMethod(EventbriteException):
    pass


class InvalidResourcePath(EventbriteException):
    pass


class UnknownEndpoint(EventbriteException):
    pass


class UnsupportedEndpoint(EventbriteException):
    pass
