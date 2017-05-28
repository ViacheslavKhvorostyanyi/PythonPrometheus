#!/usr/bin/python
import math
import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])

if z==1 and x!=0:
        c='Everybody sing a song:'+y*(' '+"la"+(x-1)*("-la"))+"!"
        print c
    
elif z==0 and x!=0:
         c='Everybody sing a song:'+y*(' '+"la"+(x-1)*("-la"))+"."
         print c
else:
    print 'Everybody sing a song:.'
   
        

    

                                    
