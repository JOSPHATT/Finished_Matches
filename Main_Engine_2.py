from Main_Engine import raw_results
import pandas as pd
import re
Raw_results=raw_results()
match_links=Raw_results[0] 
Scores=Raw_results[1]
Teams=Raw_results[2]
Time=Raw_results[3]
print(match_links, Scores, Teams, Time)

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
F_games=Finished_Games.to_dict('records')
#print(F_games)
def final_results():
    return F_games
print(final_results())
#APPENDING OUTPUT TO CSV OR DATABASE
#Finished_Games.to_csv(‘Finished_matches.csv’, mode=’a’, index=False)
###Main_Engine.py ends here....

