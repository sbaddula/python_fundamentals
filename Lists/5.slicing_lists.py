numbers = [22, 45, 55, 53, 67]

#slicing the list
first_three = numbers[:3]

#slicing from middle start at 2nd element and ending at 3rd element
#note both numbers are index numbers, the 2nd index number is exclusive.
middle_two = numbers[1:3]

#get last 2 elements
last_two = numbers[-2:]

print("first three elements", first_three)
print("middle two elements", middle_two)
print("last two elements", last_two)