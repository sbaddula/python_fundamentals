#Create the queue
queue = []

#Enqueue operation (add element)
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueue operation:", queue)

#Dequeue operation (to remove)
queue.pop(0)
print("Queue after dequeue operation:", queue)

#peek operation
first_element = queue[0]
print("First element after dequeue operation:", first_element)
print("Queue after peek operation:", queue)

#Isempty
IsEmpty = len(queue) == 0
print("Is queue empty:", IsEmpty)

#Size operation
queue_size = len(queue)
print("Current size of the queue", queue_size)