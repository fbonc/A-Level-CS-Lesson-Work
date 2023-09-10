from datetime import date

choice = input("Number of days until:\n- Your birthday (1)\n- Christmas (2)\n")
today = date.today()

def daysuntil(date):
    if date < today:
        date = date.replace(year=today.year + 1)
    time_to_date = abs(date - today)
    return time_to_date.days

if choice == "1":
    birthday = input("\nEnter your birthday in the format MM-DD: ")
    month, day = map(int, birthday.split("-"))
    birthday_date = date(today.year, month, day)
    print(f"\n{daysuntil(birthday_date)} days until your birthday")
elif choice == "2":
    christmas = date(today.year, 12, 25)
    print(f"\n{daysuntil(christmas)} days until christmas")







