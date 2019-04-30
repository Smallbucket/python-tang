#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
if match:
    print('found', match.group())
else:
    print('did not find')

