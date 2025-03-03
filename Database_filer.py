from Main_Engine import finished_games
f=finished_games()
#print(f)

# Import MySQL Connector/Python 
import mysql.connector as connector

#db_pass='Araf'

# Connect to the database
try:
    print("Establishing a new connection between MySQL and Python.")
    connection=connector.connect(user="root",password='Araf')
    print("A connection between MySQL and Python is successfully established")

except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)
connection=connector.connect(user="root",password='Araf')


# Create a cursor object to communicate with entire MySQL database
cursor = connection.cursor()

