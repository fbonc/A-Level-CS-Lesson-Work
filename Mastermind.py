import random

#---- Create Answer ----

def getAnswer():
    length = int(input("\nHow many digits do you want the answer to be? "))
    Answer = []
    for i in range(1, length + 1):
        Answer.append(str(random.randint(1,9)))
    return Answer


#---- Easy mode ----

def easyMode():
    easyQ = input("Do you want to enable easy mode (allows to see whether positions are correct)? (y/n): ")

    if easyQ == "y":
        return True
    else:
        return False


#---- Game ----

def masterMind(num):

    guess = None
    easy = easyMode()

    while guess != num:
        correct = 0
        guess = input("\nGuess a number: ")
        guess = list(guess)

        if guess == num:
            print("You win!")
            break

        else:
            if easy == False:
                for i in range(0,4):
                    if guess[i] == num[i]:
                        correct += 1
                print(f"You got {correct} number(s) correct")
            else:
                for i in range(0,4):
                    if guess[i] == num[i]:
                        print(f"You got {guess[i]} correct")



print("\n- - - - WELCOME TO MASTERMIND! - - - -\n")

while True:

    masterMind(getAnswer())

    playAgain = input("\n\nDo you want to play again? (y/n): ")

    if playAgain == "y":
        continue
    else:
        print("Good bye!")
        break



        

