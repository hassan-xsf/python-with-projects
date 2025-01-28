
class Book:
    def __init__(self , name , author):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Book Name: {self.name} | Author: {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def addBook(self , book):
        self.books.append(book)
    
    def removeBook(self , bookName):
        for b in self.books:
            if b.name == bookName:
                self.books.remove(b)
                return True
        return False
 
    def displayAllBooks(self):
        if not self.books:
            print("No books in library")
            return
        for book in self.books:
            print(book)


hassanLibrary = Library()


def menu():
    while(True):
        try:
            print("==== Hassan's Library System ====")
            print("1 - Add book")
            print("2 - Remove a book")
            print("3 - List all books")
            print("4 - Quit")
            print("=================================")
            userInput = int(input("Select your option\n"))
            
            if userInput == 1:
                bookName = input("Enter your book name\n")
                bookAuthor = input("Enter your book author\n")
                
                userBook = Book(bookName , bookAuthor)
                hassanLibrary.addBook(userBook)
                print(f"Book name: {bookName}, Author: {bookAuthor} has been added, Total books: {len(hassanLibrary.books)}")
            elif userInput == 2:
                bookName = input("Enter book name to remove\n")

                if hassanLibrary.removeBook(bookName) == False:
                    print("Book not found")
                else:
                    print(f"Book {bookName} has been removed, Total books left: {len(hassanLibrary.books)}")
            elif userInput == 3:
                hassanLibrary.displayAllBooks()
            elif userInput == 4:
                print("Thank you for staying!")
                break
            else:
                print("Invalid choice..")
        except ValueError:
            print("That's not a valid integer. Try again!")

menu()