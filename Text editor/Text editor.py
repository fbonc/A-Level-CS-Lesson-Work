import os

def readfile(filename):
    checkifexists(filename)
    with open(filename, 'r') as file:
        text = file.read()
        print(f"\nText file:\n{text}")

def writeto(filename):
    close = False
    with open(filename, 'a') as file:
        print("Text to add (write 'CLOSE' to stop writing and save the file):\n")
        while close == False:
            usertext = input("")
            if usertext == "CLOSE":
                break
            file.write(f"{usertext}\n")

def editfile(filename):
    checkifexists(filename)
    close = False
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(lines)

    with open(filename, 'w') as file:
        while close == False:
            linenum = input("Line number to edit ('CLOSE' to save and exit): ")
            if linenum == "CLOSE":
                break
            edittext = input("Text to change line to: ")
            lines[int(linenum) - 1] = (edittext + "\n")
            file.writelines(lines)

def checkifexists(filename):
    if filename not in os.listdir(os.getcwd()):
        open(filename, "x")

def deletefile(filename):
    print(os.getcwd())
    if os.path.isfile(fr"{os.getcwd()}\{filename}"):
        os.remove(fr"{os.getcwd()}\{filename}")
    else:
        print("Error: file not found")

while True:
    choice = input("\n1) Read a file\n2) Write to a file\n3) Edit a specific line of a file\n4) Delete a file from this directory\n5) Stop the program\n")
    if choice == "5":
        break
    directory = os.listdir(os.getcwd())
    print("\nFiles in directory:")
    for eachfile in directory:
        print(f"- {eachfile}")
    filename = input("Name of file (writing non-existent file creates it): ")
    if choice == "1":
        readfile(filename)
    elif choice == "2":
        writeto(filename)
    elif choice == "3":
        editfile(filename)
    elif choice == "4":
        deletefile(filename)
    else:
        continue

            

