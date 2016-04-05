#! /usr/bin/env python
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
	f = open('server-logs','rb')
	f2= open('server-logs-mod.txt','w')
	data = f.readlines()
	out = []
	orig = []
	lenv =[]
	c=0
	for row in data:
		row = row.replace('|', '')
		sdf = row.split('"')
		if ((c+1) % 500000)==0:
			print 'Iteration ', (c+1)

		if len(sdf)==3:			
			step1 = sdf[0]
			step1 = step1.split("[")[0].replace(' ','|') + step1.split("[")[1].split(":")[0]
			step2 = sdf[1].replace("GET ","").replace(" HTTP", '').replace("/1.0","").replace("/V1.0","")
			step3 = '|'.join(sdf[2].split(" ")[1:3])
			rowout = step1 +'|' + step2 + '|' + step3

		if len(sdf)==4:
			step1 = sdf[0]
			step1 = step1.split("[")[0].replace(' ','|') + step1.split("[")[1].split(":")[0]
			sdf = sdf[0] + sdf[1] + sdf[2]
			step2 = sdf[1]+sdf[2]
			step2 = step2.replace('GET ', "").replace(" HTTP/", "").replace("V1.0","").replace("1.0","")
			step3 = sdf[3].replace(' ', '|')
			rowout = step1 + '|' + step2 + step3

		if len(sdf)==5:
			step1 = sdf[0]
			step1 = step1.split("[")[0].replace(' ','|') + step1.split("[")[1].split(":")[0]
			step2 = ''.join(sdf[1:3]) 
			step3 = sdf[4].replace(' ', '|')
			rowout = step1 + step2 + step3

		if '\n' not in rowout:
			rowout  = rowout+'\n'

		f2.write(rowout)
		c+=1


if __name__ == '__main__':
	main()

print 'Processing Complete'
