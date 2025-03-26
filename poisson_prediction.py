"""import pandas as pd
import numpy as np
from scipy.stats import poisson

# Assuming df is your DataFrame with columns 'home', 'away', 'home_goals', 'away_goals'
df = pd.DataFrame({
    'home': ['Team A', 'Team B', 'Team C', 'Team D'],
    'away': ['Team B', 'Team C', 'Team D', 'Team A'],
    'home_goals': [2, 1, 3, 0],
    'away_goals': [1, 2, 1, 2]
})

# Calculate the average goals scored by each team at home and away
home_avg_goals = df.groupby('home')['home_goals'].mean()
away_avg_goals = df.groupby('away')['away_goals'].mean()

# Create a function to predict the correct score
def predict_correct_score(home_team, away_team):
    home_avg = home_avg_goals[home_team]
    away_avg = away_avg_goals[away_team]
    
    # Calculate the probability of each possible score
    scores = []
    for home_score in range(6):  # assuming a maximum of 5 goals
        for away_score in range(6):
            home_prob = poisson.pmf(home_score, home_avg)
            away_prob = poisson.pmf(away_score, away_avg)
            score_prob = home_prob * away_prob
            scores.append((home_score, away_score, score_prob))
    
    # Sort the scores by probability and return the most likely one
    scores.sort(key=lambda x: x[2], reverse=True)
    return scores[0]

# Test the function
home_team = 'Team A'
away_team = 'Team B'
predicted_score = predict_correct_score(home_team, away_team)
print(f'Predicted score: {home_team} {predicted_score[0]} - {away_team} {predicted_score[1]}')
"""
