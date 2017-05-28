#!/usr/bin/env python
import sys
param = sys.argv[1::]
param.remove("0")
param.reverse()
strf = ' '.join(param)
print strf

