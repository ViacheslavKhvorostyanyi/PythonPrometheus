#!/usr/bin/env python
# -*- coding: utf-8 -*-

#modules
import sys
#variables
num = sys.argv[1].lower().replace(" ","")
#functions
def pol(num):
	if num[::-1] == num:
		return "YES"
	else:
		return "NO"
		
print pol(num)
print num







