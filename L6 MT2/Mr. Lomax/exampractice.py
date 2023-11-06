ISBN = [None for i in range(1,14)]

for count in range(1, 14):
    num = int(input("Please enter next digit of ISBN:"))
    ISBN[count - 1] = num

CalculatedDigit = 0
Count = 1

while Count < 13:
    CalculatedDigit += ISBN[Count - 1]
    Count += 1
    CalculatedDigit += ISBN[Count - 1] * 3
    Count += 1

while CalculatedDigit >= 10:
    CalculatedDigit -= 10

CalculatedDigit = 10 - CalculatedDigit

if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == ISBN[12]:
    print("Valid ISBN")
else:
    print("Invalid ISBN")

