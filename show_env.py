#!/usr/bin/env python

from __future__ import print_function

import base64
import json
import os

ENV = os.environ.copy()


for p in sorted(ENV.items()):
    print('='.join(p))

print(base64.b64encode(json.dumps(ENV).encode('utf-8')))
