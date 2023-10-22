#!/usr/bin/env python3

###Python_06_problemset_Point#9
#Create a FASTA parser script
#template file is Python_06.fasta

fasta_parse =  open("Python_06.fasta", "r") 
fasta = fasta_parse.read()
print(fasta)

#counts number of lines
#for sequence in contents:
#	content_count = contents.count(sequence)
#print(content_count)

#count number of characters
#print(len(contents))

fastaDict = {}
for line in fasta:
	line = line.strip()
	if line.startswith(">"):
		
		
	else:
		seq +=   
			
print(contents)

#	gene_id, seq = line.split()
#	genes[gene_id] = seq
#print(genes)		
