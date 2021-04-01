class Library:

    def __init__(self, list_of_books):
        self.availableBooks = list_of_books

    def displayAvailabeBooks(self):
        print('the available books are: ')
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Yes, u have now borrowed the book {}".format(requestedBook))
            self.availableBooks.remove(requestedBook)
        else:
            print("The book is not in stock")

    def addBook(self, returnedBook):
        if returnedBook not in self.availableBooks:
            self.availableBooks.append(returnedBook)
            print("You have returned the book: {}".format(returnedBook))

class Student:

    def requestBook(self):
        print("Enter name of the book u would like to ceck out")
        self.book = input()
        return self.book
    def returnBook(self):
        print("Enter book u would like to return")
        self.book = input()
        return self.book


if __name__ == '__main__':

    library = Library(['dude', 'hero', 'jam', 'hey'])
    student = Student()
    while True:
        print("""======Library Menu=====
                1.Display all books
                2.Request a book
                3.Return a nook
                0. for exit""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            library.displayAvailabeBooks()
        elif choice == 2:
            library.lendBook(student.requestBook())
        elif choice == 3:
            library.addBook(student.returnBook())
        elif choice == 0:
            break
