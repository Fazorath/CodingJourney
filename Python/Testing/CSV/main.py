import csv 
with open("Python\\Testing\\CSV\\Program Codes.csv","r") as f:
    reader = csv.reader(f)
    classcode = {row[0] for row in reader}
    # print(classcode)

with open("Python\\Testing\\CSV\\student roster example.csv") as f:
    reader = csv.reader(f)
    rostercode = {row[5] for row in reader}
    rostercode = rostercode
    # print(rostercode)

difference = rostercode - classcode
print(difference)
