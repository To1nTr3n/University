# 5. Modify the file reader in read_smallest_skip.py of Skipping the Header, on
# page 188 so that it can handle files with no data after the header
from typing import TextIO

def skip_header(reader: TextIO) -> str:
    line = reader.readline()
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
# Now line contains the first real piece of data
    return line

def smallest_value_skip(reader: TextIO) -> int:
    line = skip_header(reader).strip() # => 55,...
    smallest = int(line)
    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)
    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))