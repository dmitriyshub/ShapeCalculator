import csv
local_file=[]

with open('db.csv', encoding='utf-8') as File:
    Reader = csv.reader(File, delimiter=',')

    for row in Reader:
        local_file.append(row)

titles = tuple(local_file.pop(0))

print(local_file)
print(titles)