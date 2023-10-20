#!/usr/bin/env python3

#Point 1
myset = set('ATGTGGG')
myset2 = {'ATGTGGG'}

print(myset)
print(myset2)

# I get: 
#{'G', 'A', 'T'} with myset, with 3 items
#{'ATGTGGG'} with myset2, with 1 item
#the {} can be used for sets but need to enumerate, cannot separate the items like set()
