filename = "L6 MT2\Mr. Lomax\google-10000-english.txt"
uword = input("What is your word: ")
wordlist = []

with open(filename, 'r') as file:
    text = file.read().split(" ")

    for word in text:
        temp = list(word)
        for letter in uword:
            if letter not in temp:
                continue
            else:
                temp.remove(letter)
        wordlist.append(word)

print(f"Words that can be made from {uword}:")
for i in wordlist:
    print(f"{i}")