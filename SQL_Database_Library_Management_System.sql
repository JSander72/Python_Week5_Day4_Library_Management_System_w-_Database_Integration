CREATE DATABASE Library_db;

create table Books (
Book_id int primary key,
Title varchar (255) not null,
Author varchar (255) not null,
Published_Year int,
Genre varchar (50),
Available_Copies int
);

create table Members (
Member_id int primary key,
Name varchar (100) not null,
Email varchar (100) unique,
Join_Date Date
);

create table Borrowed_Books (
Borrow_id int primary key,
Book_Id int,
Member_Id int,
Borrow_Date Date,
Return_Date Date,
foreign key (Book_Id) references Books (Book_Id),
foreign key (Member_Id) references Members (Member_Id)
);

Insert into Books (
Book_Id, Title, Author, Published_Year, Genre, Available_Copies) values 
(00551, 'The_Great_Gatsby', 'F_Scott_Fitzgerald', '19250410', 'Tragedy', '10000'),
(00552, 'ULYSSES', 'James_Joyce', '19220202', 'Modernist_Novel', '10000'),
(00553, 'Lolita', 'Vladimir_Nabokov', '19552001', 'Novel', '10000'),
(00554, 'Brave_New_World', 'Aldous_Huxley', '19320505', 'Science_Fiction_Dystopian_Fiction', '10000'),
(00555, 'The_Sound_And_The_Fury', 'William_Faulkner', '19290103', 'Southern_Gothic', '10000'),
(00556, 'Catch22', 'Joseph_Heller', '19611010', 'Dark_Comedy', '10000'),
(00557, 'The_Grapes_Of_Wrath', 'John_Steinbeck', '19391404', 'Novel', '10000'),
(00558, 'I_Claudius', 'Robert_Graves', '19340810', 'Historical', '10000'),
(00559, 'To_The_Lighthouse', 'Virginia_Woolf', '19270505', 'Modernism', '10000'),
(05510, 'Slaughterhouse_Five', 'Kurt_Vonnegut', '19693103', 'War_Novel', '10000'),
(05511, 'Invisible_Man', 'Ralph_Ellison', '19521404', 'African_American_Literature', '10000'),
(05512, 'Native_Son', 'Richard_Wright', '19400103', 'Social_Protest', '10000'),
(05513, 'USA_Trilogy', 'John_Dos_Passos', '19300405', 'Political_Fiction', '10000'),
(05514, 'A_Passage_To_India', 'E_M_Forster', '19240406', 'Novel', '10000'),
(05515, 'Tender_Is_The_Night', 'F_Scott_Fitzgerald', '19341204', 'Tragedy', '10000'),
(05516, 'Animal_Farm', 'George_Orwell', '19451708', 'Political_Satire', '10000'),
(05517, 'The_Golden_Bowl', 'Henry_James', '19041011', 'Philosophy', '10000'),
(05518, 'A_Handful_Of_Dust', 'Evelyn_Waugh', '19340603', 'Fiction', '10000'),
(05519, 'As_I_Lay_Dying', 'William_Faulkner', '19300302', 'Black_Comedy', '10000'),
(05520, 'The_Heart_Of_The_Matter', 'Graham_Greene', '19480302', 'Nove', '10000')
;


    
    
    
    
    