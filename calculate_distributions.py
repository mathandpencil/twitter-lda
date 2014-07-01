import numpy as np
import cPickle as pickle
import json

(ldak, phi, voca) = pickle.load(open('ldaphi_K10.p', "rb"))

words_to_column = {}
for i,w in enumerate(voca):
	words_to_column[w] = i
		
tweets = json.loads(open("results.json").read())
for tweet in tweets:
	html = tweet.get('text')
	title = tweet.get('title','').encode("ascii","ignore")
	url = tweet.get('resolvedPageUrl',"").encode("ascii","ignore")
	
	sum_vector = np.zeros(ldak)
	for word in html.split():
		word = word.lower()
		if word in words_to_column:
			sum_vector += phi[:, words_to_column[word]]
	if sum_vector.sum() == 0: 
		sum_vector = np.ones(ldak)/ldak;
	else: 
		sum_vector = sum_vector / sum_vector.sum()
		
	print "%s,%s,%s" %(",".join(["%2.3f" % s for s in sum_vector]),title,url)	
	