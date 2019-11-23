from data import *
import random
import os
import pickle
def last_scores():
    """process record of player names and player scores"""
    if os.path.exists(nom_fichier_scores):
        fichier_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else:
        scores = {}
    return scores

def record_scores(scores):
    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()


def introduction():
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

def level(player_name):
    choice_pc = word()
    print(choice_pc)
    length_word = ""
    for i in range(len(choice_pc)):
        length_word += "*"
    print("{} vous disposez de 8 essais pour deviner le mot compose de".format(player_name, length_word))
    often = 8
    inter = ""
    for i in range(len(choice_pc)):
        inter += "*"
    while often > 0 and inter!= choice_pc:
        letters_found = compare(inter, choice_pc)
        if letters_found == inter:
            often-= 1
        print(letters_found)
        inter = letters_found
    if inter == choice_pc:
        print("BRAVO! {}vous gagnez et quittez la partie avec un score de {}".format(player_name, often))
    elif often == 0:
        print("DOMMAGE {} perdu! vous quittez la partie avec un score de {}".format(player_name, often))
    return often

def play_ask():
    answer = input("voulez vous jouer? taper oui ou non").upper()#accept oui/non
    tag = ["OUI", "NON"]
    while answer not in tag:#if input different =error
        print("erreur de saisie taper oui ou non")
        answer = input("entrer votre réponce de nouveau").upper()
    return answer
