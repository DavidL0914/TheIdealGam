import sqlite3

# Connect to the database (create a new one if it doesn't exist)
import os
# Get the absolute path to the 'instance' directory

# Specify the absolute path to the database file
db_file_path = 'example.db'

# Connect to the database using the absolute path
conn = sqlite3.connect(db_file_path, check_same_thread=False)

cursor = conn.cursor()

# Create a table for user login data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
def visualize_users_data():
    conn = sqlite3.connect(db_file_path, check_same_thread=False)

    cursor = conn.cursor()
    # Fetch all rows from the 'users' table
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()
    print(users_data)
    # Print or process the data as needed
    result = []
    for user in users_data:
        result.append(f"Username: {user[0]}, Password: {user[1]}")

    # Close the connection
    conn.close()
    return result
