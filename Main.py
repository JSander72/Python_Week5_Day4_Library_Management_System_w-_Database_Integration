from enum import member
import Author
import Book
import User
import db_connect as db

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")
    Book.append(Book(title, author, genre, publication_date))
    print("Book added successfully!")

def borrow_book():
    title = input("Enter book title to borrow: ")
    user_id = input("Enter your library ID: ")
    for book in book:
        if book.get_title() == title:
            if book.borrow():
                for member_id in member:
                    if member_id.get_library_id() == user_id:
                        member_id.borrow_book(title)
                        print("Book borrowed successfully!")
                        return
                print("User not found.")
                return
            else:
                print("Book is not available.")
                return
    print("Book not found.")

def return_book():
    title = input("Enter book title to return: ")
    user_id = input("Enter your library ID: ")
    for book in book:
        if book.get_title() == title:
            if book.return_book():
                for user in Member_id:
                    if user.get_library_id() == user_id:
                        if user.return_book(title):
                            print("Book returned successfully!")
                            return
                        else:
                            print("You haven't borrowed this book.")
                            return
                print("User not found.")
                return
            else:
                print("Book is already available.")
                return
    print("Book not found.")

def search_book():
    title = input("Enter book title to search: ")
    for book in Book:
        if book.get_title() == title:
            print(f"Title: {book.get_title()}")
            print(f"Author: {book.get_author()}")
            print(f"Genre: {book.get_genre()}")
            print(f"Publication Date: {book.get_publication_date()}")
            print(f"Available: {book.is_available()}")
            return
    print("Book not found.")

def display_all_books():
    if not Book:
        print("No books in the library yet.")
    else:
        for book in Book:
            print(f"Title: {book.get_title()}, Available: {book.is_available()}")

def add_user():
    name = input("Enter user name: ")
    library_id = input("Enter library ID: ")
    Member_id.append(User(name, library_id))
    print("User added successfully!")

def view_user_details():
    library_id = input("Enter library ID: ")
    for user in Member_id:
        if user.get_library_id() == library_id:
            print(f"Name: {user.get_name()}")
            print(f"Library ID: {user.get_library_id()}")
            print(f"Borrowed Books: {user.get_borrowed_books()}")
            return
    print("User not found.")

def display_all_member():
    if not Member_id:
        print("No member_id in the library yet.")
    else:
        for user in Member_id:
            print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}")

def add_author():
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")
    Author.append(Author(name, biography))
    print("Author added successfully!")

def view_author_details():
    name = input("Enter author name: ")
    for author in author:
        if author.get_name() == name:
            print(f"Name: {author.get_name()}")
            print(f"Biography: {author.get_biography()}")
            return
    print("Author not found.")

def display_all_authors():
    if not author:
        print("No authors in the library yet.")
    else:
        for author in author:
            print(f"Name: {author.get_name()}")

while True:
    print("\nWelcome to the Library Management System!")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            book_choice = input("Enter your choice: ")

            if book_choice == '1':
                add_book()
            elif book_choice == '2':
                borrow_book()
            elif book_choice == '3':
                return_book()
            elif book_choice == '4':
                search_book()
            elif book_choice == '5':
                display_all_books()
            elif book_choice == '6':
                break
            else:
                print("Invalid choice.")

    elif choice == '2':
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all member_id")
            print("4. Back to Main Menu")

            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                add_user()
            elif user_choice == '2':
                view_user_details()
            elif user_choice == '3':
                display_all_member()
            elif user_choice == '4':
                break
            else:
                print("Invalid choice.")

    elif choice == '3':
        while True:
            print("\nAuthor: " + user_choice)