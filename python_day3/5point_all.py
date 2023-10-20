#!/usr/bin/env python3
import sys

#Point 1-4
#fav_dict = { 'book' : 'Jitterbug Perfume' , 'song' : "Tom Petty - I Won't Back Down" , 'tree' : 'Cedar' }
#print(fav_dict['book'])
#fav_thing = 'book'
#print(fav_dict[fav_thing])
#print(fav_dict['tree'})

#Point 5
favs_dict = {}
print(favs_dict)

favs_dict ['book'] = 'Jitterbug Perfum'
favs_dict ['song'] = "Tom Petty - I Won't Back Down"
favs_dict ['tree'] = 'Cedar'
favs_dict ['organism'] = 'Elephant'

print(favs_dict)
print('')

#fav_thing = 'organism'
#print(favs_dict[fav_thing])
#print('')

#Point 6
#for thing in favs_dict:
#	result = favs_dict[thing]
#	print (f'{thing:>8}', result)
#print('')

#Point 7
#fav_thing = favs_dict[sys.argv[1]]
#print(fav_thing)
#print ('')

#Point 8
#print('This are the keys: ')
#for thing in favs_dict:
#	print(thing)

#Point 9
#favs_dict['organism'] = 'dog'
#print(favs_dict)

fav_thing = favs_dict[sys.argv[1]]
favs_dict[sys.argv[1]] = 'Blackbird'
print(favs_dict)
