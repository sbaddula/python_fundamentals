#open file in append mode
with open('example.txt', 'a') as file:
    file.write('\nappending a new line to the file')
    file.close()