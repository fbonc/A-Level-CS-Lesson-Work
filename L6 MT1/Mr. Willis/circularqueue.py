class CircularQueue:
    def __init__(self):
        self._maxSize = 8
        self._queue = [None for i in range(self._maxSize)]
        self._front = -1
        self._back = -1
    
    def addItem(self, item):
        if ((self._back + 1) % self._maxSize == self._front):
            return "Queue full"

        elif self._front == -1:
            self._front = 0
            self._back = 0
            self._queue[self._back] = item
            return f"{item} inserted"
        
        else:
            self._back = (self._back + 1) % self._maxSize
            self._queue[self._back] = item
            return f"{item} inserted"

    def removeItem(self):
        if self._front == -1:
            return "Queue empty"
        
        if self._back == self._front:
            msg = f"{self._queue[self._front]} removed from front"
            self._front = -1
            self._back = -1
            return msg
        
        else:
            msg = f"{self._queue[self._front]} removed from front"
            self._front = (self._front + 1) % self._maxSize
            return msg

    def size(self):
        if self._front == -1:
            return "Queue is empty"
        
        elif self._back >= self._front:
            qSize = (self._back - self._front) + 1
            return f"Queue size is {qSize} items"

queue = CircularQueue()

print(queue.addItem(1))
print(queue.size())
print(queue.addItem(1))
print(queue.size())
print(queue.addItem(1))
print(queue.size())
print(queue.removeItem())
print(queue.size())
print(queue.removeItem())
print(queue.size())
print(queue.removeItem())
print(queue.size())


            





