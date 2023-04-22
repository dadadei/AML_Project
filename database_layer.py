import sqlite3
from sqlite3 import Error
import os

# Import the required modules and set the database file name
DB_FILE = 'data.db'

# Function to create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except Error as e:
        print(e)
    return conn

# Function to create the user_data table if it doesn't exist
def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS user_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    passport TEXT NOT NULL,
                    image_path TEXT NOT NULL,
                    extracted_text TEXT NOT NULL
                );
                '''
            )
            conn.commit()
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

# Function to store user data, image, and extracted text into the user_data table
def store_data(user_info, image, extracted_text):
    conn = create_connection()
    if conn is not None:
        try:
            # Save the image to the "images" folder
            image_path = os.path.join('images', f'{user_info["phone"]}.jpg')
            image.save(image_path)

            # Insert the user data and image path into the user_data table
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO user_data (phone, address, passport, image_path, extracted_text)
                VALUES (?, ?, ?, ?, ?);
                ''',
                (user_info['phone'], user_info['address'], user_info['passport'], image_path, extracted_text)
            )
            conn.commit()
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

# Function to query all data from the user_data table
def query_data():
    conn = create_connection()
    data = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_data;")
            rows = cursor.fetchall()

            # Convert the query results into a list of dictionaries
            for row in rows:
                data.append({
                    'id': row[0],
                    'phone': row[1],
                    'address': row[2],
                    'passport': row[3],
                    'image_path': row[4],
                    'extracted_text': row[5]
                })
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()
    return data

# Create the user_data table if it doesn't exist
create_table()

