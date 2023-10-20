#!/usr/bin/env python3

#trying out reading, writing and saving files
#file to open from shell = https://raw.githubusercontent.com/prog4biol/pfb2023/master/files/Python_06.txt

import sys

poem = open(sys.argv[1],"r")
content_poem = poem.read()

poem_upper = open('poem_upper.txt','w')
poem_upper.write(content_poem.upper())

print( "wrote to file 'poem_upper.txt'" )

poem.close()
poem_upper.close()
