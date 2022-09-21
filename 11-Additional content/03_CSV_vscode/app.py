import csv

file = open("example.csv",encoding="utf-8")

data = csv.reader(file)

lst = list(data)

for item in lst[1:6]:
   print(item)