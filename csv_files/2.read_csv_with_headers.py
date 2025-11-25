import csv

with open('example_with_headers.csv', mode='r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        print(row)
