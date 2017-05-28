#!/usr/bin/python
#import modules
import sys
#functions
def fib():
			currNumb = 1
			prevNumb = 0
			for i in range(k-1):
				nextNumb=prevNumb+currNumb
				prevNumb = currNumb
				currNumb = nextNumb 
				print currNumb
#variables
n=int(sys.argv[1])
k=0
#body
print k	
while k<n:
	k=k+1
	if k==1:
		print k		
fib()


