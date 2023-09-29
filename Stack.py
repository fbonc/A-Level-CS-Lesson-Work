stack = []

def pop(stack):
    if len(stack) > 0:
        print(f"'{stack[-1]}' removed from top of stack")
        stack.pop()
    else:
        print("Stack empty")

def push(stack):
    if len(stack) < 10:
        item = input("What item to add?")
        stack.append(item)
    else:
        print("Stack full")

def peek(stack):
    print(stack[-1])

def test_full(stack):
    if len(stack) == 10:
        print("Stack full")
    else:
        print("Not full")

def test_empty(stack):
    if len(stack) == 0:
        print("Stack empty")
    else:
        print("Not empty")

def reverse():
    temp = []
    word = list(input("What word do you want to reverse?"))
    while (len(word)): 
        temp.append(word.pop())
    print(temp)

while True:
    choice = input("\n1) Pop\n2) Push\n3) Peek\n4) Test if full\n5) Test if empty\n6) Reverse a word\n")
    if choice == "1":
        pop(stack)
    elif choice == "2":
        push(stack)
    elif choice == "3":
        peek(stack)
    elif choice == "4":
        test_full(stack)
    elif choice == "5":
        test_empty(stack)
    elif choice == "6":
        reverse()
    else:
        continue




