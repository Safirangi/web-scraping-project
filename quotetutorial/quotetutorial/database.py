import sqlite3
# THIS IS A DUMMY FILE EXPLAINING THE WAY SQLITE DATABASE IS CREATED AND USED

# creating a connection
conn = sqlite3.connect('myquotes.db') # connects to a database 'myqoutes'. if this database does not exist then it creates that database file. 

# cursor helps to take advantage of all functionalities of SQLite database package
curr = conn.cursor()

# execute() helps us execute SQL queries.
# """""" this is used to write multiple line query
curr.execute("""create table quotes_tb(
                quote text, 
                author text,
                tag text        
                )""") 

# manual insertion in the database
# cursor.execute("""insert into quotes_db values ('python is awesome', 'buildwithpython', 'python')""")

conn.commit()
conn.close()
