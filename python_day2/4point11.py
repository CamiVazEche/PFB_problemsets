#!/usr/bin/env python3

sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for sequence in sequences:
	length = len(sequence)
	index = sequences.index(sequence) + 1
	print(index, length, sequence, sep='\t')
