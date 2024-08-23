from Book import Book
from User import User
from Author import Author
import library_db_connector as mydb

books = []
users = []
authors = []

def get_books_borrowed_by_member(connection, member_name):
    cursor = connection.cursor()
    query = """
    SELECT Members.name, Books.title, Authors.name 
    FROM Members
    JOIN Borrowed_Books ON Borrowed_Books.Member_Id = Members.Member_id
    JOIN Books ON Books.Book_id = Borrowed_Books.Book_Id
    JOIN Authors ON Books.Author_Id = Authors.Author_id
    WHERE Members.name = %s
    """
    cursor.execute(query, (member_name,))
    return cursor.fetchall()

def find_members_by_book_title(connection, book_title):
    cursor = connection.cursor()
    query = """
    SELECT Books.title, Members.name, Borrowed_Books.Borrow_Date, Borrowed_Books.Return_Date
    FROM Borrowed_Books
    JOIN Books ON Books.Book_id = Borrowed_Books.Book_Id
    JOIN Members ON Members.Member_id = Borrowed_Books.Member_Id
    WHERE Books.title = %s
    """
    cursor.execute(query, (book_title,))
    return cursor.fetchall()

def insert_borrowing_record(connection, member_id, book_id, borrow_date):
    cursor = connection.cursor()
    query = """
    INSERT INTO Borrowed_Books (Member_Id, Book_Id, Borrow_Date, Return_Date)
    VALUES (%s, %s, %s, DATE_ADD(%s, INTERVAL 14 DAY))
    """
    cursor.execute(query, (member_id, book_id, borrow_date, borrow_date))
    connection.commit()

def find_overdue_books(connection):
    cursor = connection.cursor()
    query = """
    SELECT Books.title AS book_title, Members.name AS member_name
    FROM Borrowed_Books
    JOIN Members ON Members.Member_id = Borrowed_Books.Member_Id
    JOIN Books ON Books.Book_id = Borrowed_Books.Book_Id
    WHERE DATEDIFF(CURDATE(), Borrowed_Books.Borrow_Date) > 14 AND Borrowed_Books.Return_Date IS NULL
    """
    cursor.execute(query)
    return cursor.fetchall()

def calculate_average_borrow_duration(connection):
    cursor = connection.cursor()
    query = """
    SELECT Books.title, COUNT(*) AS no_of_times_borrowed,
    AVG(DATEDIFF(Borrowed_Books.Return_Date, Borrowed_Books.Borrow_Date)) AS average_duration
    FROM Borrowed_Books
    JOIN Books ON Books.Book_id = Borrowed_Books.Book_Id
    GROUP BY Books.title
    """
    cursor.execute(query)
    return cursor.fetchall()

def remove_borrowing_record(connection, borrow_id):
    cursor = connection.cursor()
    query = "DELETE FROM Borrowed_Books WHERE Borrow_Id = %s"
    cursor.execute(query, (borrow_id,))
    connection.commit()

def update_book_availability(connection, book_id, is_available):
    cursor = connection.cursor()
    query = "UPDATE Books SET availability = %s WHERE Book_id = %s"
    cursor.execute(query, (is_available, book_id))
    connection.commit()
    return cursor.rowcount

