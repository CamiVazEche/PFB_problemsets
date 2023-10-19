#!/usr/bin/env python3

#point6: return only even numbers

numbers = [101,2,15,22,95,33,2,27,72,15,52]
#print (type (numbers))

for number in numbers:
	if number % 2 == 0:
		print (number)
print('')

#point7:sort and sum of even and odds

num_sorted = sorted(numbers)
#print(num_sorted, type(num_sorted))

for num_sort in num_sorted:
	print (num_sort)
print('')

cum_sum_even = 0

for even in numbers:
	if even % 2 == 0:
		cum_sum_even += even
print (f'Sum of even numbers: {cum_sum_even}')

cum_sum_odd = 0
for odd in numbers:
	if odd % 2 != 0:
		cum_sum_odd += odd
print (f'Sum of odd numbers: {cum_sum_odd}')
