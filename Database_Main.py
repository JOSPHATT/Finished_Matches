from Main_Engine_2 import Finished_Games
import pandas as pd
import sqlite3

# define connection and cursor
Finished_Games=Finished_Games
connection = sqlite3.connect('finished_matches.db')

cursor = connection.cursor()

# create activities table

command1 = """CREATE TABLE IF NOT EXISTS
finished_games(id INTEGER, timestamp TEXT, 
HOME TEXT, AWAY TEXT, HOME_G INTEGER, AWAY_G INTEGER)"""

cursor.execute(command1)

# generate some random activities

activities = [(int(time.time()), datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), 
                randint(25, 35), randint(0, 10)),
              (int(time.time() + 1), datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), 
                randint(25, 35), randint(0, 10)),
              (int(time.time() + 2), datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), 
                randint(25, 35), randint(0, 10))]

# add 3 activities to activities table

cursor.executemany('INSERT INTO activities VALUES (null, ?, ?, ?, ?)', activities)

# commit changes

connection.commit()

# get activities

cursor.execute("SELECT * FROM activities")

# display data

results = cursor.fetchall()
print(results)

# close connection

cursor.close()
connection.close()
