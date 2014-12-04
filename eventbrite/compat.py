# -*- coding: utf-8 -*-
import sys

PY3 = sys.version_info[0] == 3
OLD_PY2 = sys.version_info[:2] < (2, 7)

if PY3:  # pragma: no cover
    from unittest.mock import patch

if OLD_PY2:  # pragma: no cover
    import simplejson as json
    import unittest2 as unittest
else:
    import json
    import unittest