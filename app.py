import streamlit as st
import sqlite3

# Fungsi untuk menghubungkan ke database SQLite
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        st.error(f"Error connecting to database: {e}")
    return conn

# Fungsi untuk membuat tabel di database
def create_table(conn):
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    age INTEGER NOT NULL
                                ); """
        conn.execute(sql_create_table)
    except sqlite3.Error as e:
        st.error(f"Error creating table: {e}")

# Fungsi untuk menyimpan data ke database
def insert_data(conn, user):
    try:
        sql_insert = ''' INSERT INTO users(name, age)
                         VALUES(?,?) '''
        cur = conn.cursor()
        cur.execute(sql_insert, user)
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error inserting data: {e}")

# Koneksi ke database
database = "example.db"
conn = create_connection(database)

# Buat tabel jika belum ada
if conn:
    create_table(conn)

# Judul aplikasi
st.title("Simple User Input to Database")

# Input dari pengguna
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, step=1)

# Tombol untuk menyimpan data
if st.button("Submit"):
    if name and age:
        insert_data(conn, (name, age))
        st.success("Data successfully saved to database!")

# Tampilkan data dari database
if st.button("Show Data"):
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        for row in rows:
            st.write(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    else:
        st.error("No connection to database.")

# Tutup koneksi database
if conn:
    conn.close()