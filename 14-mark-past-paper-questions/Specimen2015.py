def convert(decimalnum):
    curr = int(decimalnum)
    binary = ''

    while curr != 0:
        binary += str(curr % 2)
        curr = curr // 2

    return binary[::-1]

if __name__ == "__main__":

    while True:
        decimalnum = input('What number would you like to convert to binary? ')
        print(convert(decimalnum))
