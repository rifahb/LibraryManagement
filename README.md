# Library Management System  

This project is a efficient **Library Management System** designed to simplify the management of books. Built using **Python Flask** for the front end and **SQLite** for the back end, it provides a clean, user-friendly interface for performing library operations.  

---

## Key Features  

### 1. **Add Books**  
- Easily add new books to the library database.  
- Inputs include key details such as:  
  - Title  
  - Author   
  - Genre   

### 2. **Delete Books**  
- Remove books from the library system using a unique identifier (e.g., Book ID or ISBN).  
- Ensures seamless removal without affecting database integrity.  

### 3. **View Books**  
- View a complete list of all books available in the library.  
- **Search and Filters**: Locate specific books effortlessly using filters based on title, author, genre, or other attributes.  

---

## Tech Stack  

- **Frontend**: Python Flask (routes and HTML templates)  
- **Backend**: SQLite (lightweight and efficient database)  

---

## How It Works  

1. **User Interface**  
   - Built with Flask, the web application handles user interactions through intuitive HTML templates.  
   - Users can perform operations like adding, viewing, updating, and deleting books.  

2. **Database**  
   - All book records are securely stored in an SQLite database.  
   - The database ensures efficient querying and retrieval of book data, enabling fast searches and updates.  

3. **Core Operations**  
   - **CRUD Operations**: Users can seamlessly perform Create, Read, Update, and Delete operations.  
   - Flask acts as the bridge between the user interface and the database, managing user requests and database responses.  

---

## Benefits  

- **Lightweight & Fast**: The combination of Flask and SQLite ensures optimal performance even on minimal hardware.  
- **User-Friendly Interface**: Designed for simplicity, making it easy for users to manage books.  
- **Secure & Reliable**: Ensures data integrity through robust database management.  
- **Scalable**: Easily extendable to include features like user management, borrowing functionality, and overdue tracking.  

---

## Future Enhancements  

- **User Authentication**: Add login/logout functionality for administrators and users.  
- **Borrowing System**: Enable users to borrow books and track due dates.  
- **Overdue Notifications**: Send reminders for overdue books via email or SMS.  
- **Report Generation**: Generate detailed reports on book records and user activity.  

---

This Library Management System is a simple yet powerful tool to manage a collection of books, perfect for small-scale libraries, schools, or personal use.
