
def bubble(numbers):
    swap = False

    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                swap = True
                numbers[j], numbers[j+1] = numbers[j + 1], numbers[j]
        
        if not swap:
            return numbers
    
    return numbers


l1 = [10,3, 533,1]

print(bubble(l1))