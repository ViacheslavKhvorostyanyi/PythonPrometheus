#!/usr/bin/env python
#modules
import sys
#variables
key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
my_dict = {}
my_dict_rev = {}
x=0
z=0
data = sys.argv[1]
data_next = sys.argv[2]
code_curr = ""
dcryp = ""	
ln = len(alphabet)

#body

#create the ecrypted dictionary for English
for i in range (ln):
	my_dict[alphabet[x:x+1]]= key[x:x+5] 
	x+=1

#create the decrypted dictionary for English
for i in range (ln):
	my_dict_rev[key[z:z+5]] = alphabet[z:z+1]		
	z+=1
	
#print my_dict[data] - encypted 1st argv if it has only one symbol	

#loop for string in 1st argv
for i in data:
	code_curr += my_dict[i]+" "	
print code_curr	

#loop for decryted string
"""
for i in data_next:
	dcryp += my_dict_rev[i]	
	print dcryp
	"""
#replace the spaces in decryption 
data_edit =  data_next.replace(" ","")

#this loop must add " " after every five element in string,but how to do i haven't understood yet
for i in data_edit:
	i =" "+ data_edit[::5]

#print decryption
print my_dict_rev[data_edit]

