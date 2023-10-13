class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size
    
    def __str__(self):
        current = self.head.next
        msg = "\n--Top--\n"
        num = self.size - 1
        while current:
            msg += f"({num}) {current.data}\n"
            current = current.next
            num -= 1
        return f"{msg}--Bottom--\n"

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from empty stack")
        temp = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek from empty stack")
        return self.head.next.data
    

s1 = Stack()

s1.push("Bellow")
s1.push("Marrow")
s1.push("Yellow")
s1.push("Mellow")
s1.push("Jello")
s1.push("Greetings")
s1.push("Hello")
s1.push("Hi")

print(s1)

print(f"Top of stack is: {s1.peek()}")

print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

print(s1)


# Exception raised as popping/peeking from empty stack
# s1.pop()
# s1.pop()
# s1.pop()
# s1.pop()
# s1.pop() / s1.peek()
