# -*- coding: utf-8 -*-

import sys

PY3 = sys.version_info[0] == 3
OLD_PY2 = sys.version_info[:2] < (2, 7)


if PY3:
    string_type = str
else:
    string_type = basestring


try:  # pragma: no cover
    import simplejson as json
except ImportError:
    # For python 2.6
    import json

try:
    from urllib.parse import (
        urlparse,
        urljoin,
    )
except ImportError:
    from urlparse import (
        urlparse,
        urljoin,
    )
