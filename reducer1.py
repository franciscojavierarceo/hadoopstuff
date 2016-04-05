#! /usr/bin/env python
import sys

aggtable = {}
for line in sys.stdin:
	line = line.strip()
	keyout, valout = line.split("\t")
	try:
		aggtable[keyout]+=int(valout)
	except:
		aggtable[keyout]=int(valout)

print('\n'.join( [(i+' '+str(j)) for (i,j) in aggtable.items()]))
