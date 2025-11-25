numbers = [1, 2, 3, 4, 5]

#using remove() it will remove the first occurrence of value
numbers.remove(3)

numbers.insert(2, 2.5)

print(numbers)

#using pop() to remove a element at specific index
#pop allows you to capture the element being removed
popped_element = numbers.pop(2)

print(numbers)
print("popped element", popped_element)

#using del to delete an element at a specific index
#del does not allow to capture the element being deleted
del numbers[1]

print(numbers)

