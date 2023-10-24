#!/usr/bin/env python3

### I open the files and build the sets

with open("alpaca_all_genes.tsv", "r") as alpaca_all:
	all_genes_header = set(alpaca_all)
#	all_sort = sorted(all_genes_header) 
#	print(all_sort)

# Remove the header
all_genes = all_genes_header.remove("Gene stable ID\n")
all_sort = sorted(all_genes) 
print(all_sort)




### check length of the set 
#total_genes = len(all_genes)
#print(total_genes)


#with open("alpaca_pigmentation_genes.tsv","r") as alpaca_pigm:
#	pigm_genes_header = set(alpaca_pigm)
# Remove the header

#pigm_genes = pigm_genes_header.remove(Gene stable ID)

### check length of the set 
#total_pigm_genes_header = len(pigm_genes)
#print(total_pigm_genes)


#with open("alpaca_stemcellproliferation_genes.tsv","r") as alpaca_prolif:
#	prolif_genes_header = set(alpaca_prolif)
# Remove the header
# prolif_genes = prolif_genes_header.remove("Gene stable ID")

### check length of the set 
#total_prolif_genes = len(prolif_genes)
#print(total_prolif_genes)


### I find genes that are not cell proliferation genes, difference between all_genes and proliferation_genes

#non_prolif_genes = all_genes - prolif_genes
#total_non_prolif = len(non_prolif_genes)
#print(total_non_prolif)

