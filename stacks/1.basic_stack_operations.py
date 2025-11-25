#creating stack
stack = []

#push operation
stack.append(1)
stack.append(2)
stack.append(3)

print("stack after push operation:", stack)

#pop operation, removes element from the stack
stack.pop()
print("stack after pop operation:", stack)

#peek operation, does not remove the element, it is used just for accessing
top_element = stack[-1]
print("stack top element:", top_element)
print("stack after peek operation:", stack)

#is empty check
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)

#size of stack
stack_size = len(stack)
print("Stack size:", stack_size)