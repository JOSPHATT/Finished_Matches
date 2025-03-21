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

def raw_results():
    return match_links, Scores, Teams, Time



#CELL NO.2

#print(match_links)
#print(Scores)
#print(Teams)
#print(Time)

#separate home and away both for titles/names and scores
#conmbine lists into dataframe for storage and further processing
