#writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'x00\x01\x02\x03\x04')
    file.close()

with open('example.bin', 'rb') as file:
    binary_data = file.read()
    print(binary_data)
    file.close()