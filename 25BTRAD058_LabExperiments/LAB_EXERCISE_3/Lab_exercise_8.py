# Contact book using lists and dictionaries.
# Contact Book Using Lists and Dictionaries: Develop a Python program to add,
# search, update, delete, and display contact details using lists and dictionaries.
# *Analyze requirements, select suitable data structures, implement
# operations, and test correctness. (CT)
# * Apply the contact book to a personal or organizational contact
# management scenario.(RWE)

contacts = {}
while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        name = input("Name: ")
        contacts[name] = input("Phone: ")
    elif ch == 2:
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))
    elif ch == 3:
        name = input("Update name: ")
        if name in contacts:
            contacts[name] = input("New phone: ")
    elif ch == 4:
        name = input("Delete name: ")
        contacts.pop(name, None)
    elif ch == 5:
        print(contacts)
    elif ch == 6:
        break