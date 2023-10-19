#!/usr/bin/env python3

import sys

#task for point10

dna_seq = sys.argv[1]
sub_dna = dna_seq[99:201]
sub_count = sub_dna.count('g') +  sub_dna.count('G')
#sub_count = sub_dna.count('G')

print('Begin')
print (sub_dna)
print('End')
print (sub_count)
