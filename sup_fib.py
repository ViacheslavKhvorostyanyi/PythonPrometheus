#!/usr/bin/env python
import sys
a=int(sys.argv[1]) 
b=int(sys.argv[2]) 

def super_fibonacci(n, m):
	l=[]
	while m != 0:
		l.append(1)
		m-=1
	z_list=len(l)-1
	while len(l) < n:
		l.append(sum(l[-1-z_list:]))
	return(l[-1])

print super_fibonacci(a, b)
