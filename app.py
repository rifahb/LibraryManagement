from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management

# Database setup
DATABASE = "library.db"  # Database name

# Function to initialize the database and create required tables if they do not exist
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Create a users table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        # Create a books table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            available INTEGER NOT NULL)''')
        conn.commit()

# Route for the home page which redirects to the login page
@app.route("/")
def home():
    return redirect(url_for('login'))

# Route for the signup page to allow new users to register
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":  # If the form is submitted
        username = request.form['username']
        password = request.form['password']
        # Hash the password using pbkdf2:sha256 algorithm
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            try:
                # Insert the new user into the users table
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
                flash("Signup successful! Please log in.", "success")  # Success message
                return redirect(url_for('login'))  # Redirect to the login page
            except sqlite3.IntegrityError:
                flash("Username already exists. Try a different one.", "danger")  # Error message if username already exists
    
    return render_template("signup.html")  # Render the signup page

# Route for the login page where users can log in
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":  # If the form is submitted
        username = request.form['username']
        password = request.form['password']

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()

            # Check if user exists and the password matches
            if user and check_password_hash(user[2], password):
                session['user_id'] = user[0]  # Store user id in session
                session['username'] = user[1]  # Store username in session
                flash("Login successful!", "success")  # Success message
                return redirect(url_for('dashboard'))  # Redirect to the dashboard
            else:
                flash("Invalid username or password.", "danger")  # Error message for invalid login

    return render_template("login.html")  # Render the login page

# Route for the dashboard page which shows the list of books
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:  # Check if user is logged in
        return redirect(url_for('login'))  # Redirect to login if not logged in

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")  # Retrieve all books
        books = cursor.fetchall()

    return render_template("dashboard.html", books=books)  # Render the dashboard page with books

# Route for logging out the user and clearing the session
@app.route("/logout")
def logout():
    session.clear()  # Clear session data
    flash("Logged out successfully.", "success")  # Success message
    return redirect(url_for('login'))  # Redirect to the login page

# Route to add a new book to the library (only for logged-in users)
@app.route("/add_book", methods=["POST"])
def add_book():
    if 'user_id' not in session:  # Check if user is logged in
        return redirect(url_for('login'))  # Redirect to login if not logged in

    title = request.form['title']
    author = request.form['author']

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, available) VALUES (?, ?, ?)", (title, author, 1))
        conn.commit()  # Commit the changes to the database

    flash("Book added successfully!", "success")  # Success message
    return redirect(url_for('dashboard'))  # Redirect to the dashboard

# Route to delete a book from the library (only for logged-in users)
@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    if 'user_id' not in session:  # Check if user is logged in
        return redirect(url_for('login'))  # Redirect to login if not logged in

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))  # Delete the book from the database
        conn.commit()

    flash("Book deleted successfully!", "success")  # Success message
    return redirect(url_for('dashboard'))  # Redirect to the dashboard

# Route to view the list of books in the library
@app.route("/view_books")
def view_books():
    if 'user_id' not in session:  # Check if user is logged in
        return redirect(url_for('login'))  # Redirect to login if not logged in

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")  # Retrieve all books
        books = cursor.fetchall()

    return render_template("view_books.html", books=books)  # Render the books page with books

# Function to search for books by title or author
@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query', '') if request.method == 'GET' else request.form.get('query', '')
    books = []
    
    if query:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        books = cursor.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",  # Search query to find books
            ('%' + query + '%', '%' + query + '%')
        ).fetchall()
        conn.close()  # Close the database connection

    print(f"Query: {query}")  # For debugging purposes
    print(f"Books: {books}")  # For debugging purposes

    return render_template('search.html', books=books, query=query)  # Render the search page with results

# Main entry point to run the app
if __name__ == "__main__":
    init_db()  # Initialize the database on first run
    app.run(debug=True)  # Run the Flask app in debug mode
