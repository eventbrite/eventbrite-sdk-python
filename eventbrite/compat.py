# -*- coding: utf-8 -*-

import sys

PY3 = sys.version_info[0] == 3
OLD_PY2 = sys.version_info[:2] < (2, 7)

try:  # pragma: no cover
    import simplejson as json
except ImportError:
    # For python 2.6
    import json


