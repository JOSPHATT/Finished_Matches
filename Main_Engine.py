#scrape live games from https://www.betpawa.co.ke/live
#PREDICT OUTCOME LIBRARY
#SAVE FILE AS Main_Engine.py
#UNCOMMENT 'INSTALL' BELOW
#!pip install selenium

import time
import json
import datetime
import os
from selenium import webdriver
import pandas as pd
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--disable-features=NetworkService,NetworkServiceInProcess')
options.add_argument('--enable-javascript')

# Initialize the webdriver
driver = webdriver.Chrome(options=options)

# URL of the website to scrape
url = "https://www.betpawa.co.ke/live"

# Navigate to the URL
driver.get(url)

# Wait for the page to load (adjust timeout as needed)
# For multiple elements change find_element to find_elements
# and use expected_conditions.presence_of_all_elements_located instead of presence_of_element_located
try:
    WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'events-container.prematch'))
    )
except:
    print("Games container not found")
    driver.quit()
    exit()

# Find all game containers
game_containers = driver.find_elements(By.CLASS_NAME, 'events-container.prematch')

# Extract data for each game
def extract_game_data(game_containers, class_name):
  Info=[]
  for game_container in game_containers:
    # Extract game details (example - adjust selectors as needed)
    info = game_container.find_element(By.CLASS_NAME, class_name).text # Or relevant class for scores
    Info.append(info)
  return Info

def extract_match_links(game_container, class_name):
  Match_links=[]
  for game_container in game_containers:
    # Extract game details (example - adjust selectors as needed)
    el = game_container.find_element(By.CLASS_NAME, class_name)
    m_links=el.get_attribute('href') # Or relevant class for scores
    Match_links.append(m_links)
  return Match_links
match_links=extract_match_links(game_containers, 'event-match')
Scores=extract_game_data(game_containers, 'scores')
Teams=extract_game_data(game_containers, 'teams')
Time=extract_game_data(game_containers, 'times')
# Close the webdriver
driver.quit()
#print(match_links)
#print(Scores)
#print(Teams)
#print(Time)



#CELL NO.2

#print(match_links)
#print(Scores)
#print(Teams)
#print(Time)

#separate home and away both for titles/names and scores
#conmbine lists into dataframe for storage and further processing

livescores_df = pd.DataFrame({'match': Teams, 'time': Time, 'Live_score': Scores, 'match_link': match_links})
#print(livescores_df)

#function to extract time from match time data
def match_time():
  if row['time']:
    for entry in row['time'].split(","):
      s=re.split(" ? ", entry, maxsplit=2)
      c_s = re.sub(r'[^a-zA-Z0-9]', '', s[1])
      return int(c_s)
  else:
    #print("NO TIME for:", row['match'])
    return -10

#CREATING NEWDATAFRAME WITH COLUMN NAMES: [Home_team, Away_team, Home_score, Away_score, time_a, match_link]
#INITIALISING COLUMN DATA IN FORM OF LISTS WHICH ARE THEN CONVERTED TO DATAFRAME
Home_T, Away_T, Home_G, Away_G, Time_A, Match_URL=[],[],[],[],[],[]

for index, row in livescores_df.iterrows():
  match_string=row['match']
  score_string=row['Live_score']
  match_link=row['match_link']

  match_a=match_string.splitlines()
  score_a=score_string.splitlines()

  Home_team=match_a[0]
  Away_team=match_a[1]
  Home_score=score_a[0]
  Away_score=score_a[1]
  time_a=match_time()

  Home_T.append(Home_team)
  Away_T.append(Away_team)
  Home_G.append(Home_score)
  Away_G.append(Away_score)
  Time_A.append(time_a)
  Match_URL.append(match_link)

Column_Headers=['HOME', 'AWAY','H_GOALS', 'A_GOALS', 'GAME_TIME', 'MATCH_LINK']

live_matches_df = pd.DataFrame({'HOME': Home_T, 'AWAY': Away_T, 'H_GOALS': Home_G, 'A_GOALS': Away_G, 'GAME_TIME': Time_A, 'MATCH_LINK': Match_URL})
#live_matches_df.to_csv('live_matches.csv', index=True)

#FULL DATA
#print(live_matches_df)

#CAPTURE GAMES WITH LESS THAN 50 MINUTES PLAY TIME FOR SCRAPING AND PREDICTION
#ENTER CODE HERE

# filterING dataframe
finished_games=live_matches_df.query('GAME_TIME  > 90')
Finished_Games=finished_games.drop(['MATCH_LINK', 'GAME_TIME'], axis=1)
Finished_Games.reset_index(drop=True, inplace=True)

print(Finished_Games)

#APPENDING OUTPUT TO CSV OR DATABASE
#Finished_Games.to_csv(‘Finished_matches.csv’, mode=’a’, index=False)
###Main_Engine.py ends here....
