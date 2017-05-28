#!/usr/bin/ python
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
n = int(raw_input('input N:'))
flag = False
for i in range(n):
    if (i+1) % 11 == 0 and (i+1) % 2 == 0:
        flag = True
print flag
year = int(raw_input('input year:'))
print not(year % 4) and ((year % 100) or not(year % 400
