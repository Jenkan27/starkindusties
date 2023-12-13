from models import Sale
import csv

list_from_file = []

with open("100SalesRecords.csv", 'r') as file:
    csvreader = csv.reader(file)
    
    first_row = True
    for row in csvreader:
        if first_row:
            row_title = []
            for element in row:
                row_title.append(element)
            first_row = False
            continue
        row_dict = {}
        index = 0
        
        while index < len(row):
            for element in row:
                row_dict[row_title[index]] = element
                index += 1
        list_from_file.append(row_dict)

for line in list_from_file:
    print ('hej')