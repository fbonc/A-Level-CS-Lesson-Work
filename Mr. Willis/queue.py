queue = []
max = 8

def enqueue(item):
    if len(queue) == max:
        print("Queue is full")
    else:
        queue.insert(0, item)
        return item

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        item = queue[-1]
        queue.pop()
        return item

enqueue(1)
print(queue)
dequeue()
print(queue)


