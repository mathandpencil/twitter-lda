#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json

DIFF_BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXX'

def create_bulk_job(urls, name):
	apiUrl = 'http://api.diffbot.com/v3/article'
	params = dict(token=DIFF_BOT_TOKEN, name=name, urls=urls, apiUrl=apiUrl)
	response = requests.post('http://api.diffbot.com/v3/bulk',data=params)
	return json.loads(response.content)
	
if __name__ == '__main__':
	urls = " ".join([u.strip().replace('"','') for u in open(sys.argv[1]).readlines()])
	name = 'MISITI'
	print urls
	print create_bulk_job(urls=urls,name=name)
	print "go to http://api.diffbot.com/v3/bulk?token=%s&name=%s" % (DIFF_BOT_TOKEN,name)
	#
	