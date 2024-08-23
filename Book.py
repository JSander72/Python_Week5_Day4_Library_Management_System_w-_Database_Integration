
from User import User
from Author import Author
import library_db_connector as mydb

books = []
users = []
authors = []

class Book:
    # ... (existing attributes and methods)

    def save_to_db(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
        val = (self.title, self.author.id, self.isbn, self.publication_date, self.is_available)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def get_all_from_db():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM books")
        result = mycursor.fetchall()
        # Process the result and create Book objects
        return Book_id


class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True
        else:
            return False    
        
class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            return True
        else:
            return False