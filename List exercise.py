# name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']

# for i in range(3):
#     name = input("Type in a name: ")
#     name_list.append(name)

# print(name_list)
# print(f"The third name is {name_list[2]}")
# print(f"The last seven names are {name_list[-7:]}")

numbers = []
for i in range(5):
    number = int(input("Type in a number: "))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sum(numbers)/len(numbers))
