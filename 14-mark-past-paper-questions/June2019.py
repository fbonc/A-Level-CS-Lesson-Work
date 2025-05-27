def checkwords(word1, word2):

    for i in word1:
        if i in word2:
            word2.remove(i)
        else: return False

    return True


if __name__ == "__main__":
    while True:
        word1 = list(input("Enter the first word:"))
        word2 = list(input("Enter the second word:"))

        if checkwords(word1, word2) == True:
            print("The first word CAN be created from the second word")
        else:
            print("The first word CANNOT be created from the second word")
