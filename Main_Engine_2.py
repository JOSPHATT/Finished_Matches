from Main_Engine import raw_results
import pandas as pd
import re
import time

Raw_results=raw_results()
match_links=Raw_results[0] 
Scores=Raw_results[1]
Teams=Raw_results[2]
Time=Raw_results[3]

#print(match_links, Scores, Teams, Time)

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
Time_stamp, Home_T, Away_T, Home_G, Away_G, Time_A, Match_URL=[],[],[],[],[],[],[]

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
  Time_stamp.append(time.strftime('%x'))

Column_Headers=['TIME', 'HOME', 'AWAY','H_GOALS', 'A_GOALS', 'GAME_TIME', 'MATCH_LINK']

live_matches_df = pd.DataFrame({'TIME': Time_stamp, 'HOME': Home_T, 'AWAY': Away_T, 'H_GOALS': Home_G, 'A_GOALS': Away_G, 'GAME_TIME': Time_A, 'MATCH_LINK': Match_URL})

#=============APPENDING OUTPUT TO CSV FILE============

#FULL DATA
#print(live_matches_df)


#HALFTIME GAMES
#CAPTURE GAMES AT HALF TIME PLAY

live_matches_df_copy=live_matches_df
Half_time_games=live_matches_df_copy.query('GAME_TIME >= 45 & GAME_TIME <=46')
Half_Time_Games=Half_time_games.drop(['MATCH_LINK', 'GAME_TIME'], axis=1)
Half_Time_Games.reset_index(drop=True, inplace=True)
Half_Time_Games=Half_Time_Games.rename(columns={'H_GOALS': 'H_HGOALS', 'A_GOALS': 'A_HGOALS'})
#Half_Time_Games
#APPENDING OUTPUT TO CSV OR DATABASE
try:
  Half_Time_Games.to_csv('half_time_matches.csv', mode='a', header=False)
  print('NEW DATA APPENDED TO ---half_time_matches.csv-- FILE')
except:
  print('Error appending new data')
  print('new data supposed to be appended to csv file is: ', Half_Time_Games) 
  


#FINISHED GAMES
# filterING dataframe

finished_games=live_matches_df.query('GAME_TIME  > 90')
Finished_Games=finished_games.drop(['MATCH_LINK', 'GAME_TIME'], axis=1)
Finished_Games.reset_index(drop=True, inplace=True)
#APPENDING OUTPUT TO CSV OR DATABASE
try:
  Finished_Games.to_csv('Finished_matches.csv', mode='a', header=False)
  print('NEW DATA APPENDED TO ---Finished_matches.csv--- FILE')
except:
  print('Error appending new data')
  print('new data supposed to be appended to csv file is: ', Finished_Games) 
  
###Main_Engine.py ends here....

