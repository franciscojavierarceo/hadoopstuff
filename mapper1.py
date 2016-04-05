#! /usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip()

	try:
		statuscode = line.split("|")[5]
	except:
		statuscode = '-'

	results = [statuscode, "1"]
	print("\t".join(results))
