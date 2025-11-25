try:
    with open('file.txt', 'r') as file:
        file_content = file.read()

except FileNotFoundError:
    print('File not found')
except IOError:
    print('Error occurred while reading the file')
