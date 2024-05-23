import csv

with open("./read_a_file/data.csv") as data_file:
    data = csv.reader(data_file)
    
    temp = []
    for row in data:
        temp.append(row[1])
        print(row)

print(temp)