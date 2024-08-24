import db_connect as mydb

def get_books_borrowed_by_member(connection, member_name):
    cursor = connection.cursor()
    query = """
    SELECT Members.Name, Books.Title, Books.Author 
    FROM Members
    JOIN Borrowed_Books ON Borrowed_Books.Member_Id = Members.Member_Id
    JOIN Books ON Books.Book_Id = Borrowed_Books.Book_Id
    WHERE Members.Name = %s
    """
    cursor.execute(query, (member_name,))
    return cursor.fetchall()

def find_members_by_book_title(connection, book_title):
    cursor = connection.cursor()
    query = """
    SELECT Books.Title, Members.Name, Borrowed_Books.Borrow_Date, Borrowed_Books.Return_Date
    FROM Borrowed_Books
    JOIN Books ON Books.Book_Id = Borrowed_Books.Book_Id
    JOIN Members ON Members.Member_Id = Borrowed_Books.Member_Id
    WHERE Books.Title = %s
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
    SELECT Books.Title AS book_title, Members.Name AS member_name
    FROM Borrowed_Books
    JOIN Members ON Members.Member_Id = Borrowed_Books.Member_Id
    JOIN Books ON Books.Book_Id = Borrowed_Books.Book_Id
    WHERE DATEDIFF(CURDATE(), Borrowed_Books.Borrow_Date) > 14 
    AND Borrowed_Books.Return_Date IS NULL
    """
    cursor.execute(query)
    return cursor.fetchall()

def calculate_average_borrow_duration(connection):
    cursor = connection.cursor()
    query = """
    SELECT Books.Title, COUNT(*) AS no_of_times_borrowed,
    AVG(DATEDIFF(Borrowed_Books.Return_Date, Borrowed_Books.Borrow_Date)) AS average_duration
    FROM Borrowed_Books
    JOIN Books ON Books.Book_Id = Borrowed_Books.Book_Id
    GROUP BY Books.Title
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
    query = "UPDATE Books SET Available_Copies = Available_Copies + %s WHERE Book_Id = %s"
    cursor.execute(query, (is_available, book_id))
    connection.commit()
    return cursor.rowcount

