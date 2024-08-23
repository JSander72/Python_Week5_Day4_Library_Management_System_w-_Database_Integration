from Book import Book
from User import User
from Author import Author
import library_db_connector as mydb

books = []
users = []
authors = []


class User:
    # ... (existing attributes and methods)

    def save_to_db(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        val = (self.name, self.library_id)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def get_all_from_db():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users")
        result = mycursor.fetchall()
        # Process the result and create User objects
        return users_list

    @staticmethod
    def get_by_id(user_id):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = mycursor.fetchone()
        if result:
            # Create a User object from the result
            return user_obj
        else:
            return None

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def return_book(self, book_title):
        if book_title in self.__borrowed_books:
            self.__borrowed_books.remove(book_title)
            return True
        else:
            return False