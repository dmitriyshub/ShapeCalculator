import csv
from collections import Counter

local_db=[]

with open('db.csv', encoding='utf-8') as File:
    Reader = csv.reader(File, delimiter=',')

    for row in Reader:
        local_db.append(row)

titles = tuple(local_db.pop(0))

classified = []
for row in local_db:
    classified.append(row[-1])
    #print(classified)
for row in local_db:
    print(row)



counter_object = Counter(classified)
keys = counter_object.keys()
num_values = len(keys)
print(keys)
print(num_values)


print(local_db)
print(titles)