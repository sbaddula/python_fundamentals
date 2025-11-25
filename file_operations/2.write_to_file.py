#open a file in write mode
with open('example.txt', 'w') as file:
    file.write('Hello World!\n')
    file.write('welcome to file I/O operations')
    file.close()
