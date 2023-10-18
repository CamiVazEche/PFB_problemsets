#!/usr/bin/env python3
import sys

DNA_seq = sys.argv[1]
Eco_start_dig = DNA_seq.find('GAATTC')
Eco_start = (Eco_start_dig+1)
Eco_end = (Eco_start+5)

print(f'EcoRI startPos:{Eco_start} endPos:{Eco_end}')
