# Student data manager using files.
# * Student Data Manager Using Files: Develop a Python program to store, retrieve, search, update, and
# display student records using file operations.
# * Design appropriate record-management logic, select suitable file operations, validate inputs, and test data
# retrieval and updates. (CT)
# * Apply the program to a college student-record management scenario and explain its usefulness in
# maintaining student information. (RWE)

while True:
    print("\n1.Add 2.Display 3.Search 4.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Name: ")
        marks = input("Marks: ")
        with open("students.txt", "a") as f:
            f.write(name + "," + marks + "\n")
    elif ch == 2:
        with open("students.txt", "r") as f:
            print(f.read())
    elif ch == 3:
        name = input("Search name: ")
        with open("students.txt", "r") as f:
            for line in f:
                if line.startswith(name + ","):
                    print(line)
            else:
                print("Not found")
    elif ch == 4:
        break