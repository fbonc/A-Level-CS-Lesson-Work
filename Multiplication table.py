table = input("What multiplication table would you like to view?")

while table.isdigit() == False:
    table = input("Please enter an integer")

def calculatetable(table):
    for i in range(1,13):
        print(f"{table} x {i} = {table*i}")

calculatetable(table)


# table = int(input("What multiplication table would you like to view?"))
# for i in range(1,13):
#     print(f"{table} x {i} = {table*i}")