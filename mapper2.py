#! /usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()
	tmp = line.split("|")
	month = tmp[3].split("/")[1]
	try:
		bytes = tmp[6]
	except:
		bytes = 0
	if bytes=='-':
		bytes = 0
	results = [month, str(bytes)]
	print("\t".join(results))
