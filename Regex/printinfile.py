import re

def findprint():
    with open(r'C:\Users\felip\Desktop\School\CS\Lesson Work\Mastermind game.py') as file:
        text = file.read()

    matches = re.finditer('(?:print[(])(.*)(?:[)])', text)
    print(matches)
    for match in matches:
        for group in match.groups():
            print(group)

def findquotations():
    with open(r'dracula.txt') as file:
        text = file.read()

    matches = re.finditer('(.{10})(?:")(.*)(?:")(.{10})', text)
    print(matches)
    for match in matches:
        print(match)

def capitalletters():
    with open(r'dracula.txt') as file:
        text = file.read()

    matches = re.finditer('(?:[^.?!] )([A-Z][a-z]+)', text)
    print(matches)
    for match in matches:
        for group in match.groups():
            print(group)

# findprint()
# findquotations()
capitalletters()