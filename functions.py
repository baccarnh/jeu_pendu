from data import *
import random
import os
import pickle
def recup_scores():
    """process record of player names and player scores"""
    if os.path.exists(nom_fichier_scores): # Le fichier existe
        # On le récupère
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores

def enregistrer_scores(scores):
    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()


def presentation():
    while True:
        name = input("veuillez saisir votre nom")
        if name.isalpha():
            break
        print("veuillez saisir un nom contenant que des lettres")
    print("le nom du joueur est {}".format(name.upper()))
    return name

def word():
    return (random.choice(liste_words)).upper()

def letter():
    while True:
        letter_chosen = input("veuillez saisir votre lettre")
        if letter_chosen.isalpha():
            break
        print("veuillez saisir une lettre")
    print("la lettre choisie par le joueur est {}".format(letter_chosen.upper()))
    return letter_chosen.upper()

def compare(inter, choice_pc):
    result=""
    choice_player = letter()
    if choice_player not in choice_pc:
        print("la lettre choisie n existe pas dans le mot a deviner")
    else:
        for i in range(len(choice_pc)):
            if choice_pc[i] == choice_player and inter[i]=="*":
                result+=choice_player
            elif inter[i]!="*":
                result+=inter[i]
            else:
                result+="*"
        inter=result
    return inter

def level():
    scores=recup_scores()
    player_name=presentation()
    if player_name not in scores.keys():
        scores[player_name]=0
    choice_pc = word()
    print(choice_pc)
    length_word = ""
    print("vous disposez de 8 essais pour deviner le ")
    for i in range(len(choice_pc)):
        length_word += "*"
    print(length_word)
    ofen = 0
    inter = ""
    for i in range(len(choice_pc)):
        inter += "*"
    while ofen < 8 and inter!=choice_pc:
        letters_found = compare(inter, choice_pc)
        if letters_found==inter:
            ofen+=1
        print(letters_found)
        inter = letters_found
    score_player = 0
    if ofen < 8: score_player += 8 - ofen
    print("le score du joueur {} sur cette partie est de {}".format(player_name, score_player))
    scores[player_name]+=score_player
    enregistrer_scores(scores)
    play_again()


def play_again():
    answer = input("voulez vous jouer de nouveau? taper oui ou non").upper()#accept oui/non
    tag=["OUI", "NON"]
    while answer not in tag:#if input different =error
        print("erreur de saisie taper oui ou non")
        answer = input("entrer votre réponce de nouveau").upper()
    if answer=="OUI":
        print("les scores sont remis à zéros".center(50))
        level()
    if answer=="NON":
        print("Merci Aurevoir".center(50))
