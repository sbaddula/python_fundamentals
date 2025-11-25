numbers = {1, 2, 3, 4, 5}

numbers.add(6)
numbers.add(12)
numbers.add(32)

print(numbers)

numbers.remove(12)
#discard removes the element, but if not found will not throw error
numbers.discard(12)
print(numbers)
