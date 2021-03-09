from sys import argv, exit
import csv
import re

if len(argv) != 3:
    print("Incorrect input. Please provide csv file and text file")
    exit(1)

dic = {}  # creating dictionary to save information from csv file
# Open csv file and take str sequences from it as seq
with open(argv[1], "r") as str_file:
    reader = list(csv.reader(str_file))
    reader[0].remove("name")
    seq = reader[0]
    for r in range(1, len(reader)):
        name = reader[r][0]
        reader[r].remove(name)
        value = reader[r]
        dic.update({name: value})

# Open txt file
with open(argv[2], "r") as dna_file:
    dna = dna_file.read().rstrip('\n')

extract = []  # list of values, extracted from txt file
for s in seq:
    group = re.findall(f'(?:{s})+', dna)
    if not group:
        print("No match")
        exit(2)
    biggest = str(int(len(max(group, key=len)) / len(s)))
    extract.append(biggest)

# go through values in dictionary and compare with extracted value
for name, value in dic.items():
    if extract == value:
        print(name)
        exit(0)
    else:
        continue
print("No match")