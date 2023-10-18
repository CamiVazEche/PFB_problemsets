#!/usr/bin/env python3
import sys

count = int(sys.argv[1]) #the input in the unix command line is a number, so I need to explicitly tell that this is an integer
print (count)

if count > 0:
        print ('positive')
        if count < 50:
                print ('is smaller than 50')
                if (count % 2) == 0:
                        print ('it is an even number')
        if count > 50:
                print ('is bigger than 50')
                if (count % 2) == 0:
                        print ('it is divisible by 3')
                else:
                        print ('it is not divisible by 3')
        if count == 50:
                print ('this is 50!')

elif count == 0:
        print ('count equals 0')

else:
        print ('negative')
