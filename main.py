from library_books import library_books
from datetime import date, datetime, timedelta


# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def display_available_books():
    available_books = library_books #Making another copy of the same library so we don't affect the original.
    
    for availablity, books in enumerate(available_books):
        if available_books[availablity]["available"] == False: #Checks if the book is not available.
            available_books.pop(availablity) #Gets rid of the unavailable books, leaving only the available books in the library.
    
    for books in available_books: #Going to print out the copied library that consist of available books. 
        print("--------------------") #Dividers between each book when print.
        for key, value in books.items():
            if key == "id" or key == "title" or key == "author": #Only printing out the id, title, and author of each book.
                print(f'{key}: {value}')

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_book(searching):
    search = str(searching)
    list_of_books = "" #Empty string: what we are going to return.
    for keyterm, books in enumerate(library_books):
        book = str(library_books[keyterm]["title"]) 
        author = str(library_books[keyterm]["author"])
        genre = str(library_books[keyterm]["genre"])
        if author.lower().__contains__(search.lower()) or genre.lower().__contains__(search.lower()): #check to see if search matches with any keyterms in author or genre.
            list_of_books += book+"\n" #Add the book title to a string list.
    
    return list_of_books

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    #display_available_books()
    keyterm = input("Search Book by Author or Genre: ")
    print(search_book(keyterm))

    pass
