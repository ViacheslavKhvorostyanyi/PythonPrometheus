#!/usr/bin/env python
import sys
sum = 0
x = sys.argv[1]
y = sys.argv[2]
y = int(y) - int(x)
for p in range(y+1):
	x = list(str(0)*(6-len(list(x)))+str(''.join(list(x))))
	a = int(x[0]) + int(x[1]) + int(x[2])
	b = int(x[3]) + int(x[4]) + int(x[5])
if a == b:
	sum = sum + 1
	x = str(int(''.join(x)) + 1)
else:
	x = str(int(''.join(x)) + 1)
print sum
