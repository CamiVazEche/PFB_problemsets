#!/usr/bin/env python3

myset1 = {3, 14, 15, 9, 26, 5, 35, 9}
myset2 = {60, 22, 14, 0, 9}

print(myset1)
print(myset2)
print('')

#Intersection
intersect = myset1 & myset2
print('intersection: ', intersect)
print('')

#Differencce
diff_AnotB = myset1 - myset2
print('diff A not B: ', diff_AnotB)
print('')

diff_BnotA = myset2 - myset1
print('diff B not A: ', diff_BnotA)
print('')

#Union
union = myset1 | myset2
print('union: ', union)
print('')

#Symmetrical difference
sym_diff = myset1 ^ myset2
print('simm difference: ', sym_diff)
print('')
