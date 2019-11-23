
import os
import pickle
from functions import *
from data import *

scores=last_scores()
player_name=introduction()

if player_name not in scores.keys():
    scores[player_name]=0

question=play_ask()
while question=="OUI":
    player_score=level(player_name)
    scores[player_name]+=player_score
    print(scores[player_name])
    question=play_ask()
record_scores(scores)
