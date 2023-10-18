#!/usr/bin/env python3

import sys
import string

dna_seq = sys.argv[1]
dna_upper = dna_seq.upper()

dna_comp = dna_upper.replace('A','%temp%').replace('T','A').replace('%temp%','T').replace('C','%temp%').replace('G','C').replace('%temp%','G')

print ('complementary sequence:' + dna_comp)

dna_comp_rev = dna_comp[::-1]

print ('reversed complementary sequence:' + dna_comp_rev)
