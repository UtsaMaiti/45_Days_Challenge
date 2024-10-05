class Book:
    def __init__(self, bookNo, bookname, author):
        self.bookNo = bookNo
        self.bookname = bookname
        self.author = author
        self.issued = False

    def __str__(self):
        return (f'Book Number: {self.bookNo}\n'
                f'Book Name: {self.bookname}\n'
                f'Author: {self.author}\n'
                f'Status: {"Issued" if self.issued else "Available"}')


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        print(f"{book.bookname} added to the library.")

    def delBook(self, bookNo):
        for book in self.books:
            if book.bookNo == bookNo:
                self.books.remove(book)
                print(f"{book.bookname} removed from the library.")
                return
        print(f"No book found with Book Number: {bookNo}")

    def issue_book(self, bookNo):
        for book in self.books:
            if book.bookNo == bookNo:
                if not book.issued:
                    book.issued = True
                    print(f"{book.bookname} issued.")
                    return
                else:
                    print(f"{book.bookname} is already issued.")
                    return
        print(f"No book found with Book Number: {bookNo}")

    def return_book(self, bookNo):
        for book in self.books:
            if book.bookNo == bookNo:
                if book.issued:
                    book.issued = False
                    print(f"{book.bookname} returned.")
                    return
                else:
                    print(f"{book.bookname} was not issued.")
                    return
        print(f"No book found with Book Number: {bookNo}")

    def bookList(self):
        print("Books available in the library:")
        for book in self.books:
            print(book)


def myMain():
    obj = Library()
    while True:
        choice = input("Enter your choice (Add, Remove, Issue, Return, List, Exit): ").strip().capitalize()
        
        if choice == 'Add':
            bookNo = input("Enter book number: ")
            bookname = input("Enter book name: ")
            author = input("Enter author name: ")
            newBook = Book(bookNo, bookname, author)
            obj.addBook(newBook)
        
        elif choice == 'Remove':
            bookNo = input("Enter book number to remove: ")
            obj.delBook(bookNo)
        
        elif choice == 'Issue':
            bookNo = input("Enter book number to issue: ")
            obj.issue_book(bookNo)
            
        elif choice == 'Return':
            bookNo = input("Enter book number to return: ")
            obj.return_book(bookNo)
        
        elif choice == 'List':
            obj.bookList()
        
        elif choice == 'Exit':
            print("Exiting the library system.")
            break
        
        else:
            print("!INVALID CHOICE!")


if __name__ == "__main__":
    myMain()
