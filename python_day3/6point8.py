#!/usr/bin/env python3

fastq = open("Python_06.fastq.txt", "r")
contents = fastq.read()
#print(contents)

content_to_list = contents.split('@')

print(content_to_list)


#total_char_count = []
#total_line_count = 0

#for line in contents:
#	line = line.rstrip()
	
#	line_count = len(line)
#	total_char_count.append(len(line))
#	total_line_count += 1

#print(total_char_count)
#print(total_line_count)

#	line_count = line.count(line)
#	total_lines += line_count
#		seq_fastq_replace.write
#
#	seq_fastq = seq_fastq_raw.replace('+', '/n')
#
# for line in seq_fastq:
#	line = line.rstrip()
#	line_count = line.count(line)
	
#print(line_count)

