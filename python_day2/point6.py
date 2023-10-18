#!/usr/bin/env python3

import sys

#point6
dna_seq = sys.argv[1] #will take input from the command line

print(f"A={dna_seq.count('A')}") #will give the total count of each nucleotide
print(f"C={dna_seq.count('C')}") 
print(f"G={dna_seq.count('G')}")
print(f"T={dna_seq.count('T')}")

