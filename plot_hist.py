#! /usr/bin/env python
from matplotlib import pyplot as plt

f = open('plotdata.txt','rb')
day, count =[], []
for row in f:
	i, j = row.split('\t')
	day.append(i)
	count.append(int(j.replace('\n','')))

plt.hist(count)
plt.title('Number of Requests Made in a day for every day in the month of October')
plt.savefig('hist.png')
