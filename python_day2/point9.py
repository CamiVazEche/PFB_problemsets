#!/usr/bin/env python3

import sys

#point9

dna_seq = sys.argv[1]

dna_A = dna_seq.count('A')
dna_T = dna_seq.count('T')

DNA_AT = dna_A + dna_T

print(DNA_AT) 
