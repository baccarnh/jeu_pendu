from functions import *
from data import *





scores=recup_scores()
player_name=presentation()
if player_name not in scores.keys():
    scores[player_name]=0
score_player=level(player_name)
scores[player_name]+=score_player
enregistrer_scores(scores)
play_again(player_name)