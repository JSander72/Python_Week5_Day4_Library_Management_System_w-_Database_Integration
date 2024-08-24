import db_connect as mydb

class Author:
    # ... (existing attributes and methods)

    def save_to_db(self):
        mycursor = mydb.cursor()
        sql = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        val = (self.name, self.biography)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def get_all_from_db():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM authors")
        result = mycursor.fetchall()
        # Process the result and create Author objects
        return Author

    @staticmethod
    def get_by_id(author_id):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
        result = mycursor.fetchone()
        if result:
            # Create an Author object from the result
            return Author
        else:
            return None

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography