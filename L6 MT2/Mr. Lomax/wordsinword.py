filename = "L6 MT2\Mr. Lomax\google-10000-english.txt"
uword = input("What is your word: ").lower()
wordlist = []


uword_counts = {char: uword.count(char) for char in set(uword)}

with open(filename, 'r') as file:
    text = file.read().split("\n")

    for word in text:
        temp = list(word)
        if all(word.count(char) <= uword_counts.get(char, 0) for char in word):
            wordlist.append(word)

print(f"Words that can be made from {uword}:")
for i in wordlist:
    print(i)