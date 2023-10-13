f = -1
r = -1
length = 8
queue = []

def showvalues(f, r):
    print(f"Front of queue pointer: {f}")
    print(f"Rear of queue pointer: {r}")

def additem(f, r):
    itemtoadd = input("What integer do you want to add to the queue?")
    if f == -1 and r == -1:
        f = 0
        r = 0
        queue.append(itemtoadd)
    else:
        if r + 1 == length:
            print("Queue full")
        else:
            r += 1
            queue.append(itemtoadd)

def removeitem(f, r):
    if (f == -1) and (r == -1):
        print("Queue empty")
    else:
        item = queue[f]
        if f == r:
            f = -1
            r = -1
        else:
            f += 1
        print(f"{item} removed from front of queue")

def testempty(f, r):
    if r == -1 and f == -1:
        print("Queue empty")
    else:
        print("Not empty")

def testfull(r):
    if r == length:
        print("Queue full")
    else:
        print("Not full")

while True:
    choice = input("\n1) Show rear and front values\n2) Add an item to rear of queue\n3) Remove item from front of queue \n4) Test if empty\n5) Test if full\n6) Exit\n")
    if choice == "1":
        showvalues(f, r)
    elif choice == "2":
        additem(f, r)
    elif choice == "3":
        removeitem(f, r)
    elif choice == "4":
        testempty(f, r)
    elif choice == "5":
        testfull(r)
    else:
        continue