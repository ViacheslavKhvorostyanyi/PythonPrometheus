#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  geany_first.py
#  
#  Copyright 2017 Unknown <slavapro@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import math
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

def main():
	
	

	if z==1 and x!=0:
			c='Everybody sing a song:'+y*(' '+"la"+(x-1)*("-la"))+"!"
			print c
		
	elif z==0 and x!=0:
			 c='Everybody sing a song:'+y*(' '+"la"+(x-1)*("-la"))+"."
			 print c
	else:
		print 'Everybody sing a song:.'
	   
	return 0

main()
