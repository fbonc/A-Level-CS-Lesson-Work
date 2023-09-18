tasks = []

def viewtasks():
    print("TASKS:")
    for i in tasks:
        print(f"{tasks.index(i) + 1}) {i}")
    choices()
	
def addtask():
    tasks.append(input("Task to add: "))
    choices()
	
def checknexttask():
    print(f"Next task: {tasks[0]}")
    choices()
	
def completenexttask():
    print(f"Task '{tasks[0]}' completed.")
    del tasks[0]
    choices()
	
def quittaskmanager():
    print("- - - QUIT - - -")
	
menu = {"1" : ("View tasks", viewtasks),
		"2" : ("Add a task", addtask),
		"3" : ("Check the next task", checknexttask),
		"4" : ("Mark next task as completed", completenexttask),
		"5" : ("Quit", quittaskmanager)
        }
	
def choices():
    print("\nOptions:")
    for i in menu.keys():
        print(f"{i}) {menu[i][0]}")
    choice = input("Choose an option (1-5): ")
    menu.get(choice)[1]()
	
choices()


