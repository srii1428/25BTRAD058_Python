# Library management system.
# * Develop a Python program using classes and objects to manage books, issue and return books, and
# maintain availability status.
# * Identify suitable classes and attributes, implement methods, apply inheritance where appropriate, and test
# book availability and issue/return conditions
# * Simulate library operations and demonstrate how the system supports book tracking and efficient resource
# management.

class Library:
    def __init__(self, book):
        self.book = book
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book not available")
    def return_book(self):
        self.available = True
        print("Book returned")
    def display(self):
        print(self.book, "Available:", self.available)
b = Library("Python Programming")
b.display()
b.issue()
b.display()
b.return_book()
b.display()