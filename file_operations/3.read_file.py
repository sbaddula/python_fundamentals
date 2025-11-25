#open file in read mode
with open('example.txt', 'r') as file:
    #read entire file
    content = file.read()
    print(content)
    print('-------------------------------')

    #read the first line from the file
    file.seek(0)
    line = file.readline()
    print(line)

    #read the file content into a list
    file.seek(0)
    lines = file.readlines()
    print(lines)

    file.close()