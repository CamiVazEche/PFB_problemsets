#!/usr/bin/env python3

import sys

#I will input start=3 and end=10 on the shell

start = int(sys.argv[1])
end = int(sys.argv[2]) + 1

for num in range(start, end):
	if num % 2 == 0:
		print(num)
