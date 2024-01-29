def buble(numbers):
    swap = False
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                swap = True
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        if not swap:
            return
        

l1 = [5,4,3,2,1]
buble(l1)
print(l1)