#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup as bs4

global rnk
rnk = {}

def fetchQuant(gvn):
	url = 'https://www.quantcast.com/top-sites/US?jump-to=' + str(gvn)
	req = urllib2.urlopen(url)
	res = req.read()
	sou = bs4(res, 'html.parser')
	fin = []
	stt = (gvn - 100) + 1

	for elm in sou.findAll('td', {'class' : 'link'}):
        	ent = elm.text.strip()
        	fin.append(ent)

	for int in range(stt, (gvn + 1)):
        	idt = int - stt
        	if fin[idt] != 'Hidden profile':
                	rnk[int] = fin[idt]

rks = [100, 200, 300, 400, 500]

for rkk in rks:
	fetchQuant(rkk)
	print('[-] Fetched: ' + str(rkk))

for ent in rnk:
       	print('[-] Rank: ' + str(ent) + ' | ' + rnk[ent])
