#!/usr/bin/env python3
import sys

#First build a dictonary
genes = {}
seq_read = open(sys.argv[1],"r")	
for line in seq_read:
		line = line.rstrip()
		gene_id, seq = line.split()
		genes[gene_id] = seq
print(genes)
print('')

#Open new file to write

#with open("seq_revcomp.txt","w") as seq_write:
for gene in genes:
	seq = genes[gene]
	if nt in seq:
		nt1 = seq.replace('A','T')
	elif ntT in nt:
		nt1 = seq.replace('T','A')
	elif ntC in nt:
		nt1 = seq.replace('C','G')
	else:
		ntG = seq.replace('G','C')

print(f"new sequences: {genes}")

seq_read.close()

#print(seq_write)
#print(genes)
#print(seq_revcomp.txt)


exit()
#print ('complementary sequence:' + dna_comp)

#dna_comp_rev = dna_comp[::-1]

#print ('reversed complementary sequence:' + dna_comp_rev)
