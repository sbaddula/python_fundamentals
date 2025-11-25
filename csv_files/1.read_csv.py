import csv

#open a CSV a file
with open('example.csv', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    #iterate through the row and print each row
    for row in csv_reader:
        print(row)