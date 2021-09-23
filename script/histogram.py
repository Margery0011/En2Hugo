import sys
import csv
import matplotlib.pyplot as plt
import re

number_column = int(re.split("-f", sys.argv[1])[1])
file_draw = sys.argv[2]


with open(file_draw) as file:
    raw = csv.reader(file)
    lines = [line for line in raw]

data = []
for line in lines:
    if line[0] == "":
        continue
    data.append(line[number_column-1])

plt.figure()
plt.hist(data)
plt.show()
plt.savefig('histogram.png')
