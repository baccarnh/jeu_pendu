
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
    print("Vous cumulez un score total de {}" .format(scores[player_name]).center(100))
    record_scores(scores)
    question=play_ask()
    if question=="NON":
        print("MERCI AUREVOIR".center(120))
