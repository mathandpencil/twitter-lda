#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys
import json
import nltk

STOP_WORDS = nltk.corpus.stopwords.words('english')
CORPUS_FILE = open("corpus.txt", "w")

#[u'lastCrawlTimeUTC', u'date', u'title', u'diffbotUri', u'text', u'author', u'html', u'resolvedPageUrl', u'humanLanguage', u'pageUrl', u'timestamp', u'images', u'docId',

tweets = json.loads(open("results.json").read())
for tweet in tweets:
	print '----> ', tweet.get("title","")
	html = tweet.get("text","")
	words = html.split()
	words = [x.lower() for x in words if re.match('^[\w-]+$', x) is not None] # take only alphanumerics
	words = [word.lower() for word in words]
	words = [word for word in words if word not in STOP_WORDS]
	
	CORPUS_FILE.write(" ".join(words) + "\n")
	
CORPUS_FILE.close()