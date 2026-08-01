
import csv


file = open("/OSTAD/File Handling/example.csv", "r")

read = csv.reader(file)
for r in read:
    print(r)
    
