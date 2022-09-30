'''
Duo XeraRedStar: Hui Wang, William Vongphanith
SoftDev
K05 -- Bitstream
2022-09-28
Time Spent: 
'''

'''
DISCO:
random has a built in function random.choices which weights the chances of getting elements from an array
QCC:

HOW THIS SCRIPT WORKS: 

'''

import random
import csv

with open('occupations.csv', newline='') as csvfile:
    occupations = list(csv.reader(csvfile))

print(occupations)

jobs = {}
for i in range(1, len(occupations) - 1):
    