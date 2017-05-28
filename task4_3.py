#!/usr/bin/env python
#modules
import sys
#variables
str1 = str(sys.argv[1])
ln = len(str1)
mark1=0
mark2=0
#body

if ln ==1:
	print "NO"
elif ln == 0:
	print "YES"
else:	
	if ln%2==0 and str1.find("(")==0:
		for i in str1:
			if i.find("(")!=-1:
				mark1+=1
			else:
				mark2+=1
		if mark1==mark2:
			print "YES"	
		else:
			 print	"NO"
	else:
		print "NO"	



