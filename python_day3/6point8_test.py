total_line_count = 0
total_char_count = []
with open("Python_06.fastq", "r") as file_input:
    for line in file_input:
        line = line.rstrip()

        total_char_count.append(len(line))
        total_line_count += 1
        
print(f"Total number of lines: {total_line_count:d}")
print(f"Total number of characters: {sum(total_char_count):d}")
print(f"Average line length: {sum(total_char_count) / total_line_count:f}")
