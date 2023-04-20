import sqlite3
from sqlite3 import Error
import os

# Database file
DB_FILE = 'data.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except Error as e:
        print(e)
    return conn

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

def store_data(user_info, image, extracted_text):
    conn = create_connection()
    if conn is not None:
        try:
            image_path = os.path.join('images', f'{user_info["phone"]}.jpg')
            image.save(image_path)

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

def query_data():
    conn = create_connection()
    data = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_data;")
            rows = cursor.fetchall()
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

# Create the table if it doesn't exist
create_table()
import sqlite3

# Function to connect to the database
def connect_to_database():
    conn = sqlite3.connect('data.db')
    return conn

# Function to create necessary tables
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, phone TEXT, address TEXT, passport TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS images
                      (id INTEGER PRIMARY KEY, user_id INTEGER, image BLOB, text TEXT,
                       FOREIGN KEY(user_id) REFERENCES users(id))''')
    conn.commit()

# Function to insert user data into the 'users' table
def insert_user_data(conn, user_info):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (phone, address, passport) VALUES (?, ?, ?)',
                   (user_info['phone'], user_info['address'], user_info['passport']))
    conn.commit()
    return cursor.lastrowid

# Function to insert image data into the 'images' table
def insert_image_data(conn, user_id, image, text):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO images (user_id, image, text) VALUES (?, ?, ?)',
                   (user_id, image.read(), text))
    conn.commit()

# Function to store data in the database
def store_data(user_info, image, text):
    conn = connect_to_database()
    create_tables(conn)
    user_id = insert_user_data(conn, user_info)
    insert_image_data(conn, user_id, image, text)
import sqlite3
from sqlite3 import Error
import os

# Database file
DB_FILE = 'data.db'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
    except Error as e:
        print(e)
    return conn

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

def store_data(user_info, image, extracted_text):
    conn = create_connection()
    if conn is not None:
        try:
            image_path = os.path.join('images', f'{user_info["phone"]}.jpg')
            image.save(image_path)

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

def query_data():
    conn = create_connection()
    data = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_data;")
            rows = cursor.fetchall()
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

# Create the table if it doesn't exist
create_table()
    conn.close()
