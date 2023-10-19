#!/usr/bin/env python3

#I follow all the steps in the hangouts

taxa = ('sapiens,erectus,neanderthalensis')
print (taxa)

#it will print the 2nd character in the string
print (taxa [1])

#it will print 'string'
print ( type(taxa) )
print ('') 

species = taxa.split(',')
print (species)

#it will print erectus
print(species[1])

#it will print list
print ( type(species) )
print ('')

#sort alphabetically
print (sorted(species))

#sort by length of string
print(sorted(species, key=len))
