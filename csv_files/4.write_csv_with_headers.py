import csv

#data to write
data = [
    {'Name': 'Raj', 'Age': '30', 'City': 'London'},
    {'Name': 'Pushpa', 'Age': '25', 'City': 'Los Angeles'},
    {'Name': 'Priya', 'Age': '35', 'City': 'Chicago'}
]

with open('output_with_headers.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csv_writer.writeheader()

    for row in data:
        csv_writer.writerow(row)

csvfile.close()
