#!/usr/bin/python

import sys
import re
import fileinput
import csv

number_change = int(re.split("-f", sys.argv[1])[1])
file_change = sys.argv[2]

id_name = {}
with open("Homo_sapiens.GRCh37.75.gtf") as file1:
    lines = file1.readlines()

for line in lines:
    gene_id = re.findall('gene_id \"(.*?)"', line)
    gene_name = re.findall('gene_name \"(.*?)"', line)
    if gene_name:
        if gene_id:
            id_name[gene_id[0]] = gene_name[0]

with open(file_change) as file2:
    data = csv.reader(file2)
    lines = [line for line in data]

gene_name_change = []
for i in range(len(lines)):
    if lines[i][0] == "":
        print(lines[i])
        continue
    gene_id_change = re.split('\.', lines[i][number_change-1])[0]
    if gene_id_change in id_name:
        lines[i][number_change-1] = id_name[gene_id_change]
        print(lines[i])

with open("changed.csv", 'w') as file2:
    writer = csv.writer(file2)
    writer.writerows(lines)

