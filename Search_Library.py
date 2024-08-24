import db_connect as mydb

def find_most_popular_genre(connection):
    cursor = connection.cursor()
    query = """
    SELECT Books.genre, COUNT(*) AS total_borrow
    FROM Books
    JOIN Borrowed_Books ON Borrowed_Books.Book_Id = Books.Book_id
    GROUP BY Books.genre
    ORDER BY total_borrow DESC
    LIMIT 1
    """
    cursor.execute(query)
    return cursor.fetchone()

def find_top_borrowers(connection):
    cursor = connection.cursor()
    query = """
    SELECT Members.name, COUNT(Borrowed_Books.Borrow_Id) AS total_borrow
    FROM Borrowed_Books
    JOIN Members ON Members.Member_id = Borrowed_Books.Member_Id
    GROUP BY Members.name
    ORDER BY total_borrow DESC
    LIMIT 5
    """
    cursor.execute(query)
    return cursor.fetchall()
