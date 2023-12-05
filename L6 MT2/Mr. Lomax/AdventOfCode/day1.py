filename = "L6 MT2\Mr. Lomax\AdventOfCode\day1input.txt"
test = "two1nine eightwothree abcone2threexyz xtwone3four 4nineeightseven2 zoneight234 7pqrstsixteen"

def findSum(text):
    textlist = text.split()
    total = 0
    for i in textlist:
        for j in i:
            if j.isnumeric():
                num1 = j
                i.replace(j, "", 1)
                break
        for j in reversed(i):
            if j.isnumeric():
                num2 = j
                break
        
        num = f"{num1}{num2}"

        total += int(num)

    print(total)
    

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def tuple1(tup):
    return tup[0]


def findSum2(text):
    textlist = text.split()
    total = 0
    for i in textlist:
        num_list = []

        for j, k in numbers.items():
            if j in i:
                pos = i.find(j)
                num_list.append((pos, j))
            if str(k) in i:
                pos = i.find(str(k))
                num_list.append((pos, k))   
        num_list.sort(key=tuple1)
        print(num_list)


        if not isinstance(num_list[0][1], int):
            num1 = numbers[num_list[0][1]]
        else:
            num1 = num_list[0][1]

        if not isinstance(num_list[-1][1], int):
            num2 = numbers[num_list[-1][1]]
        else:
            num2 = num_list[-1][1]


        num = f"{num1}{num2}"
        total += int(num)

    print(total)


def wholeFileSearch():
    with open(filename, 'r') as file:
        findSum2(file.read())


wholeFileSearch()




