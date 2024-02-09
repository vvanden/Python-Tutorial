# Create an empty list to store instances of the Student class
books = []

class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def update_avail(self, available):
        self.available = available

# Function to find a student by name
def find_book_by_title(title):
    for book in books:
        if book.title == title:
            return book
    return None

#setting initial condition
req_active = True

while req_active:
    req = input("Book Database, would you like to (A)dd a book, (S)et availability, (C)heck availability, (E)xit:").lower()
    if req == "a":
        print("**ADD A BOOK**")
        title = str(input("Title: "))
        author = str(input("Author: "))
        while True:
            try:
                available = str(input("Available (Y)es, (N)o: ")).lower()
            except available != "y" and available != "n":
                print("Sorry, I didn't understand that.")
                continue
            else:
                break
        books.append(Book(title, author, available))
    elif req == "s":
        print("**SET AVAILABILITY**")
        book_title = input ("Book title:")
        book = find_book_by_title(book_title)
        if book_title:
            while True:
                try:
                    book_availability = str(input ("Input book availability:" )).lower()
                except book_availability != "y" and available != "n":
                    print("Sorry, I didn't understand that.")
                    continue
                else:
                    break
            book_availability = book_availability.upper()
            book.update_avail(book_availability)
        else:
            print(f"Book with title '{book_title}' not found.")
    elif req == "c":
        book_title = input ("Book title:")
        book = find_book_by_title(book_title)
        if book:
            print("**BOOK STATUS**")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Available: {book.available}")
        else:
            print(f"Book with title '{book_title}' not found.")
    elif req == "e":
        print("Good bye.")
        req_active = False
    else:
        print("Sorry, I didn't understand that.") 
        continue