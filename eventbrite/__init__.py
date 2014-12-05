# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Daniel Greenfeld'
__email__ = 'danny@eventbrite.com'
# __version__ = '3.0.0-alpha5'

from ._version import __version__

try:
    from .client import Eventbrite
    from .utils import EVENTBRITE_API_URL
except ImportError:
    # Avoiding the setup.py bootstrap problem
    pass