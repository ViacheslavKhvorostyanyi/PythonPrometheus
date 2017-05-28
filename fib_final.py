#!/usr/bin/python
import math
import sys
n=int(sys.argv[1])

if n==0:
	print n
elif n>=1:		
	def fib():
		 a,b = 1,1
		 for i in range(n-1):
		  a,b = b,a+b
		 return a
	print fib()
