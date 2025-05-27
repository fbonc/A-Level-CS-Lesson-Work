import math

def question5(num):
    if num <= 1:
        return "Not greater than 1"
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return f"Is not prime"
        
        return "Is prime"


if __name__ == "__main__":
    while True:
        user_num = input("Enter a number: ")
        print(question5(int(user_num)))

        choice = input("Enter another number? (Y/N): ").lower()
        if choice != 'y':
            break
        