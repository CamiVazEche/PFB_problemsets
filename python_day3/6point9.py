#!/usr/bin/env python3

### Python_06_problemset_Point#9
### Create a FASTA parser script
### template file is Python_06.fasta

#fasta_parse =  open("Python_06.fasta", "r") 
#fasta = fasta_parse.read()
#print(fasta)

#counts number of lines
#for sequence in contents:
#content_count = contents.count(sequence)
#print(content_count)

#count number of characters
#print(len(contents))

fastaDict = {}

with open("Python_06.fasta","r") as fasta:
	for line in fasta:
		line = line.rstrip()
		if ">" in line:
			pre_gene_ID = line
			gene_ID = pre_gene_ID.replace (">","")
			fastaDict[gene_ID] = ""
		else:
			seq = line
			fastaDict[gene_ID] += seq
		
print(fastaDict)
