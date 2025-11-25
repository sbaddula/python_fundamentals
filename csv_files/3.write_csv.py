import csv

#Data for the file
data = [
    ['Name', 'Age', 'City'],
    ['Raj', '30', 'Delhi'],
    ['Pushpa', '25', 'Bengaluru'],
    ['Priya', '35', 'Chennai']
]

with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    for row in data:
        csv_writer.writerow(row)

csvfile.close()
