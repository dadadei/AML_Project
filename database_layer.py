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
    conn.close()
