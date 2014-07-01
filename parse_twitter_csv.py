#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys

for line in open(sys.argv[1]).readlines():
	results = re.search("(?P<url>https?://[^\s]+)", line.strip())
	if results:
		print results.group("url")
