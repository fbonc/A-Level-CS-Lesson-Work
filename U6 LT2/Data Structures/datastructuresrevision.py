class Stack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.memory = [None] * size
        self.top = 0
    
    def add(self, data: str) -> bool:
        if self.top == self.size - 1:
            print("Stack is full")
            return False
        self.memory[self.top] = data
        self.top += 1
        return True

    def remove(self) -> str:
        temp = self.memory[self.top - 1]
        if self.top == 0:
            print("Stack is empty")
            return False
        self.top -= 1
        return temp
    
    def peek(self) -> str:
        if self.top == self.size:
            print("Stack is empty")
            return False
        return self.memory[self.top - 1]
    
    def display(self):
        print(self.memory[:self.top])
        print(f"Top pointer: {self.top}")
    

class LinearQueue:
    def __init__(self, size: int) -> None:
        self.memory = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, data: str) -> bool:
        self.memory[self.rear] = data
        self.rear += 1
        return True

    def dequeue(self) -> str:
        temp = self.memory[self.front]
        if self.front == self.rear:
            print("Queue is empty")
            return False
        self.front += 1
        return temp
    
    def peek(self) -> str:
        if self.front == self.rear:
            print("Queue is empty")
            return False
        return self.memory[self.front]
    
    def tidy(self):
        to_i = 0
        for from_i in range(self.front, self.rear):
            self.memory[to_i] = self.memory[from_i]
        to_i += 1
        self.rear = to_i
        self.front = 0

    def display(self):
        print(self.memory[self.front : self.rear])
        print(f"Front pointer: {self.front}")
        print(f"Rear pointer: {self.rear}")


if __name__ == "__main__":
    queue = LinearQueue(10)
    queue.enqueue("Hello")
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())

    queue.enqueue("Hello")
    queue.enqueue("Hello")
    queue.enqueue("Hello")
    queue.enqueue("Hello")
    queue.enqueue("Hello")
    queue.enqueue("No")
    queue.display()
