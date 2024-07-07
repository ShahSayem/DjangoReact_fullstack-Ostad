# CSV: Comma Separated Value

import csv

fileName = "data.csv"
fileName2 = "data2.csv"

with open(fileName, "+r") as csvFile:
    csvReader = csv.reader(csvFile)

    for row in csvReader:
        print(row)


employees = [
    ['Name', 'Age', 'Department', 'Salary'],
    ['Shah Sayem', 24, 'IT', 50000],
    ['Alal', 34, 'Sales', 60000],
    ['Shafkath', 45, 'HR', 65000],
    ['Ohi', 40, 'IT', 70000],
]

with open(fileName2, "+w", newline="") as csvFile:
    csvWriter = csv.writer(csvFile)

    csvWriter.writerows(employees)