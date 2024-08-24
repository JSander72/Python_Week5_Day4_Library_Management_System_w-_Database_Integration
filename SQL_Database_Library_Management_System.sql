-- error handling
DELIMITER $$

CREATE PROCEDURE CreateLibraryDB()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction if an error occurs
        ROLLBACK;
        SELECT 'An error occurred, rolling back the transaction.' AS Error;
    END;

    -- Start transaction
    START TRANSACTION;

    
    CREATE DATABASE IF NOT EXISTS Library_db;

    -- Switch to the new database
    USE Library_db;

    -- Books table
    CREATE TABLE IF NOT EXISTS Books (
        Book_id INT PRIMARY KEY,
        Title VARCHAR(255) NOT NULL,
        Author VARCHAR(255) NOT NULL,
        Published_Year INT,
        Genre VARCHAR(50),
        Available_Copies INT
    );

    -- Members table
    CREATE TABLE IF NOT EXISTS Members (
        Member_id INT PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Email VARCHAR(100) UNIQUE,
        Join_Date DATE
    );

    -- Borrowed_Books table
    CREATE TABLE IF NOT EXISTS Borrowed_Books (
        Borrow_id INT PRIMARY KEY,
        Book_Id INT,
        Member_Id INT,
        Borrow_Date DATE,
        Return_Date DATE,
        FOREIGN KEY (Book_Id) REFERENCES Books (Book_id),
        FOREIGN KEY (Member_Id) REFERENCES Members (Member_id)
    );

    -- Insert data into Books table
    INSERT INTO Books (Book_Id, Title, Author, Published_Year, Genre, Available_Copies) VALUES 
    (551, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Tragedy', 10000),
    (552, 'Ulysses', 'James Joyce', 1922, 'Modernist Novel', 10000),
    (553, 'Lolita', 'Vladimir Nabokov', 1955, 'Novel', 10000),
    (554, 'Brave New World', 'Aldous Huxley', 1932, 'Science Fiction Dystopian Fiction', 10000),
    (555, 'The Sound and the Fury', 'William Faulkner', 1929, 'Southern Gothic', 10000),
    (556, 'Catch-22', 'Joseph Heller', 1961, 'Dark Comedy', 10000),
    (557, 'The Grapes of Wrath', 'John Steinbeck', 1939, 'Novel', 10000),
    (558, 'I, Claudius', 'Robert Graves', 1934, 'Historical', 10000),
    (559, 'To the Lighthouse', 'Virginia Woolf', 1927, 'Modernism', 10000),
    (5510, 'Slaughterhouse-Five', 'Kurt Vonnegut', 1969, 'War Novel', 10000),
    (5511, 'Invisible Man', 'Ralph Ellison', 1952, 'African American Literature', 10000),
    (5512, 'Native Son', 'Richard Wright', 1940, 'Social Protest', 10000),
    (5513, 'USA Trilogy', 'John Dos Passos', 1930, 'Political Fiction', 10000),
    (5514, 'A Passage to India', 'E. M. Forster', 1924, 'Novel', 10000),
    (5515, 'Tender is the Night', 'F. Scott Fitzgerald', 1934, 'Tragedy', 10000),
    (5516, 'Animal Farm', 'George Orwell', 1945, 'Political Satire', 10000),
    (5517, 'The Golden Bowl', 'Henry James', 1904, 'Philosophy', 10000),
    (5518, 'A Handful of Dust', 'Evelyn Waugh', 1934, 'Fiction', 10000),
    (5519, 'As I Lay Dying', 'William Faulkner', 1930, 'Black Comedy', 10000),
    (5520, 'The Heart of the Matter', 'Graham Greene', 1948, 'Novel', 10000);

    
    COMMIT;
    SELECT 'Database and tables created successfully, and data inserted.' AS Success;

END$$

DELIMITER ;


CALL CreateLibraryDB();
