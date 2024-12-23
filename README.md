# Library Management System

This project is a simple **Library Management System** designed to streamline the management of books. It features a front-end interface built using **Python Flask**, ensuring a user-friendly and responsive design. The back end is powered by **SQLite**, a lightweight and efficient database system.

## **Key Features**
1. **Add Books**
   - Users can add new books to the library database.  
   - Inputs include book details such as title, author, ISBN, genre, and publication year.

2. **Delete Books**
   - Users can remove books from the library system by specifying the book ID or other identifiers.  
   - Ensures database integrity by handling deletion requests properly.

3. **View Books**
   - Displays a list of all available books in the library.  
   - Provides filters or search functionality to quickly find specific books.

## **Tech Stack**
- **Frontend:** Python Flask (for routes and templates)  
- **Backend:** SQLite (to store book data)  

## **How It Works**
- Flask serves as the bridge between the user interface and the database, handling user requests and returning the appropriate responses.  
- The SQLite database stores all the book records securely, ensuring efficient querying and data retrieval.  
- Users can perform CRUD operations (Create, Read, Update, Delete) seamlessly via the web interface.
