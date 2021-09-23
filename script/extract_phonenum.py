#usr/bin/python/bin/python

import sys
import re
import fileinput

phonenum = {}
numinput = sys.argv[1]
phone = []
phoneregex = []
for line in fileinput.input(numinput):
    phone_t = re.findall(r'\(?0\d{2,3}[)-]?\d{7,8}', line)
    if phone_t:
        phone.append(phone_t)
print(phone)
