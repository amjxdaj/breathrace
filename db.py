import mysql.connector

conn=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'amjad@2004',
    database = 'max_breath'
)
conn.autocommit = True
cursor = conn.cursor()
# cursor.execute('create database Max_Breath')
# cursor.execute('create table auth(username varchar(20) primary key, name varchar(20), password varchar(20))')
# cursor.execute("""
#     CREATE TABLE breath_data (
#         username VARCHAR(20),
#         duration INT,
#         PRIMARY KEY (username),
#         FOREIGN KEY (username) REFERENCES auth(username) ON DELETE CASCADE
#     )
# """)
