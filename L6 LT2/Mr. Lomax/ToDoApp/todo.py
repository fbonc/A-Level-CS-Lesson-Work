import sqlite3

def show_tasks(connection):

    query = '''
    SELECT *
    FROM Tasks
    '''

    results = connection.execute(query)

    for row in results:
        msg = f'{row[0]}: '
        for i in row[1:]:
            if not i:
                msg += "✘"
            elif i == 1:
                msg += "✔"
            else:
                msg += f"{str(i)} | "
        print(f"{msg}")


def add_task(connection):

    description = ""
    while description == "":
        description = input("Enter the task description: ")

    category = ""
    while category == "":
        category = input("Enter the task category: ")

    query = '''
    INSERT INTO Tasks(Description, Category, Completed)
    VALUES(?,?,0)
    '''

    params = (description, category)
    connection.execute(query, params)


def complete_task(connection):
    task = int(input("Choose a TaskID to mark as completed: "))

    query = '''
    UPDATE Tasks
    SET Completed = 1
    WHERE TaskID = ?
    '''

    params = (task,)
    connection.execute(query, params)


def delete_task(connection):
    task = int(input("Choose a TaskID to delete: "))

    query = '''
    DELETE FROM Tasks
    WHERE TaskID = ?
    '''

    params = (task,)
    connection.execute(query, params)


def sql_search(connection):
    query = input("Enter the query: ")


    result = connection.execute(query)
    print("\nTaskID | Description | Category | Completed")
    print(*result)


if __name__ == "__main__":
    print("----- WELCOME TO YOUR TO DO LIST -----")

    while True:
        print("S: Show tasks")
        print("A: Add task")
        print("M: Mark a task as completed")
        print("D: Delete a task")
        print("SQL: Search your tasks using SQL")
        choice = input("Choose an option: ").lower()

        connection = sqlite3.connect(r'L6 LT2\Mr. Lomax\ToDoApp\tasks.db')

        print("\n")
        if choice == "s": show_tasks(connection)

        elif choice == "a": add_task(connection)

        elif choice == "m": complete_task(connection)

        elif choice == "d": delete_task(connection)

        elif choice == "sql": sql_search(connection)
        print("\n")

        connection.commit()
        connection.close() 