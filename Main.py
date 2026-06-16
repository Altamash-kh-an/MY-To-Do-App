import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

while True:
    print("\n===== TO DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Edit Task")
    print("5. Search Task")
    print("6. Mark Task as Done")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")

        cursor.execute(
    "INSERT INTO tasks (task, status) VALUES (?, ?)",
    (task, "Pending")
)

        conn.commit()

        print("✅ Task Added!")

    elif choice == "2":

        cursor.execute("SELECT * FROM tasks")

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No tasks found!")
        else:
            print("\nTasks:")
            for row in rows:
             print(f"{row[0]}. {row[1]} - {row[2]}")
    elif choice == "3":

        task_id = int(input("Enter task ID: "))

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()

        print("❌ Task Deleted!")

    elif choice == "4":

        task_id = int(input("Enter task ID: "))
        new_task = input("Enter new task: ")

        cursor.execute(
            "UPDATE tasks SET task = ? WHERE id = ?",
            (new_task, task_id)
        )

        conn.commit()

        print("✅ Task Updated!")

    elif choice == "5":

        search = input("Enter search term: ")

        cursor.execute(
            "SELECT * FROM tasks WHERE task LIKE ?",
            (f"%{search}%",)
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("No matching task found!")
        else:
            for row in rows:
                print(f"{row[0]}. {row[1]}")

    
    elif choice == "6":

      task_id = int(input("Enter task ID: "))

      cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Done", task_id)
      )
     
      conn.commit()

      print("✅ Task Marked Done!")
     
    elif choice == "7":
     print("Goodbye!")
     break

     

    else:
        print("Invalid choice!")

conn.close()