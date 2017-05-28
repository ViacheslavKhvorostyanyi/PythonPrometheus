#!/usr/bin/env python
import sys
a=str(sys.argv[1])
for i in range(len(a)/2): 
	a=a.replace('()','') 
if a.find('(') or a.find(')')= in a:
	print 'NO' 
else:
	print 'YES'

print a
