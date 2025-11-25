import csv

try:
    #open a file which does not exist
    with open('doesnotexist.csv', mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        #iterate through the row and print each row
        for row in csv_reader:
            print(row)

except FileNotFoundError:
    print('File not found')
except IOError:
    print('Error occurred while reading file')
