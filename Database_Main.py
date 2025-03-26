from Main_Engine_2 import Finished_Games
import pandas as pd
import sqlite3

# define connection and cursor
connection = sqlite3.connect('finished_matches.db')

cursor = connection.cursor()

# create activities table

command1 = """CREATE TABLE IF NOT EXISTS
finished_games(id INTEGER, timestamp TEXT, 
HOME TEXT, AWAY TEXT, HOME_G INTEGER, AWAY_G INTEGER)"""

cursor.execute(command1)

# EXTRACT LAST TWO ROWS FOR TESTING
Test_Finished_Games=tail(Finished_Games, n =2)

# add 3 GAMes to finished_games table

cursor.executemany('INSERT INTO finished_games VALUES (?, ?, ?, ?, ?, ?)', Test_Finished_Games)

# commit changes

connection.commit()

# get activities

cursor.execute("SELECT * FROM finished_games")

# display data

results = cursor.fetchall()
print(results)

# close connection

cursor.close()
connection.close()
