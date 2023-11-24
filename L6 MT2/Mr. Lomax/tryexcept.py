usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled_if(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError: 
        print("Didn't enter a number")
        number = 1

    try:   
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        if number < 0:
            msg = "using first item"
        elif number > len(usernames) - 1:
            msg = "using last item"
        print(f"List index out of range, {msg}")

    try:
        division = 301 / number
    except ZeroDivisionError:
        division = 301/1
    print(f"301 divided by {number} = {division}")





def login_unhandled_tryexcept(usernumber):
    print("\n -- The Basic Version --\n")
    if usernumber.isnumeric():
        number = int(usernumber)
    else: 
        print("Didn't enter a number")
        number = 1

    if number < 0:
            msg = "using first item"
    elif number > len(usernames) - 1:
            msg = "using last item"
    print(f"List index out of range, {msg}")
    print("Welcome", usernames[number], "user number", number,".")

    if number != 0:
        division = 301 / number
    else:
        division = 301/1
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_unhandled_tryexcept(inp)