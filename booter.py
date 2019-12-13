from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from numpy import array
import os
import numpy as np
import time
attributes = []

##ENTER LIVE GAME DATA HERE##

INNING = 2
VIS_SCORE = 3
HOME_SCORE =  2
HOME_PITCHER_ERA = 4.62
AWAY_PITCHER_ERA =5.42
HOME_ELO = 1546.5 #Team Elo as found on fivethirteight's mlb section
AWAY_ELO = 1520.13 #Team Elo as found on fivethirteight's mlb section
HOME_START_PITCHER_RATING = 1545 #Pitcher rating as found on fivethirteight's mlb section
AWAY_START_PITCHER_RATING = 1518.866 #Pitcher rating as found on fivethirteight's mlb section
GB_HOME = 0.5 #Home - games back from first in league
HOME_RS = 9 #Home - runs scored this season
HOME_RA = 8 #Home - runs allowed this season
GB_AWAY = 0
AWAY_RS = 12
AWAY_RA = 8

#HOME_WINS = 1
#HOME_LOSSES = 1
#HOME_WINPER = 0.5
#HOME_PITCHER_BB = 45
#AWAY_PITCHER_BB = 40
#HOME_PITCHER_HR = 14
#AWAY_PITCHER_HR = 25
#AWAY_WINS = 2
#AWAY_LOSSES =  0
#AWAY_WINPER = 1.0


attributes.append(INNING)
attributes.append(VIS_SCORE)
attributes.append(HOME_SCORE)
attributes.append(HOME_PITCHER_ERA)
attributes.append(AWAY_PITCHER_ERA)
#attributes.append(HOME_PITCHER_BB)
#attributes.append(AWAY_PITCHER_BB)
#attributes.append(HOME_PITCHER_HR)
#attributes.append(AWAY_PITCHER_HR)
attributes.append(HOME_ELO)
attributes.append(AWAY_ELO)
attributes.append(HOME_START_PITCHER_RATING)
attributes.append(AWAY_START_PITCHER_RATING)
#attributes.append(GB_HOME)
attributes.append(HOME_RS)
attributes.append(HOME_RA)
#attributes.append(HOME_WINS)
#attributes.append(HOME_LOSSES)
#attributes.append(HOME_WINPER)
#attributes.append(GB_AWAY)
attributes.append(AWAY_RS)
attributes.append(AWAY_RA)
#attributes.append(AWAY_WINS)
#attributes.append(AWAY_LOSSES)
#attributes.append(AWAY_WINPER)

attributesM = array([attributes])

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

predictions = loaded_model.predict_classes(attributesM)
probability = loaded_model.predict_proba(attributesM)

print("The home team is predicted to have a " + str(probability[0][0] * 100)[0:5] + "% chance of winning the game.")
print("The away team is predicted to have a " + str((1 - probability[0][0]) * 100)[0:5] + "% chance of winning the game.")


'''
testGameFile = open("testGame.txt","w+")
first = True
for att in attributes:
    if first:
        testGameFile.write(str(att))
        first = False
    else:
        testGameFile.write(", " + str(att))

testGameFile.close()
'''
#mat = np.matlib.zeroes(25,1)

#mat[0,1] = 

#7 = inning ,9 = vis score,10 = home score,60 =erahome, 61 = eraAway, 62 = bbhome, 63 = bbaway, 64 = hrhome, 65 = hraway, 72 = elo1pre, 73 = elo2pre, 78 = rating1_pre, 79 = rating2_pre, 93-98 records data home, 102-107 records data away

#mat[0] = 
