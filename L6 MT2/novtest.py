word1 = list(input("Enter the first word: "))
word2 = list(input("Enter the second word: "))

def checkWords(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
        else:
            word2.remove(letter)
    return True


# Post exam review (trying a different method)

# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")


# def checkWords2(word1, word2):
#     alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     word1pool = [0] * 26
#     word2pool = [0] * 26

#     for i, j in enumerate(alpha):
#         if j in word1.upper():
#             word1pool[i-1] += 1

#     for i, j in enumerate(alpha):
#         if j in word2.upper():
#             word2pool[i-1] += 1

#     for i, j in enumerate(word2pool):
#         if word2pool[i-1] < word1pool[i-1]:
#             return False
    
#     return True


#-------




if checkWords(word1, word2) == True:
    print("First word can be created using letters from the second word")
else:
    print("First word cannot be created using letters from the second word")