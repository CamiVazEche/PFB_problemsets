#!/usr/bin/env python3

import sys

#point7

dna_seq = sys.argv[1]

DNA = dna_seq.upper()
DNA_TU = DNA.replace('T','U')

print(DNA_TU) 
