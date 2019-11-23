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
    fichier_scores = open(nom_fichier_scores, "wb")
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()


def introduction():
    while True:
        name = input("Veuillez saisir votre nom")
        if name.isalpha():#to accept only letters!
            break
        print("Veuillez saisir un nom contenant que des lettres")
    print("Le nom du joueur est {}".format(name.upper()).center(100))
    return name.upper()

def word():
    return (random.choice(liste_words)).upper()# machine choice from a list of words in data file

def letter():
    while True:
        letter_chosen = input("Veuillez saisir votre lettre")
        if letter_chosen.isalpha() and len(letter_chosen) == 1:#accept only one letter
            break
        print("Veuillez saisir une lettre")
    print("La lettre choisie par le joueur est {}".format(letter_chosen.upper()))
    return letter_chosen.upper()

def compare(inter, choice_pc):
    result=""
    choice_player = letter()
    if choice_player not in choice_pc:
        print("La lettre choisie n'existe pas dans le mot à deviner")
    else:
        for i in range(len(choice_pc)):
            if choice_pc[i] == choice_player and inter[i]=="*":
                result+=choice_player
            elif inter[i]!="*":
                result+=inter[i]# allow us to add the new letter found in several letters all ready foud
            else:
                result+="*"
        inter=result
    return inter # inter is a middle string to increase found letters

def level(player_name): #is a one level of the game
    choice_pc = word()
    length_word = ""
    for i in range(len(choice_pc)):
        length_word += "*"# to obtain the word presentation
    print("{} vous disposez de 8 essais pour deviner le mot compose de {}".format(player_name,length_word).center(100))
    often = 8# the player can try 8 letters
    #inter = ""
    #for i in range(len(choice_pc)):
    #    inter += "*"
    while often > 0 and length_word!= choice_pc:
        letters_found = compare(length_word, choice_pc)
        if letters_found == length_word:
            often-= 1
        print(letters_found)
        length_word = letters_found
    if length_word == choice_pc:
        print("BRAVO! {} Vous gagnez et quittez la partie avec un score de {}".format(player_name, often).center(70))
    elif often == 0:
        print("DOMMAGE {} perdu! vous quittez la partie avec un score de {}".format(player_name, often).center(70))
    return often

def play_ask():# function that ask player if he want to play one level
    answer = input("voulez vous jouer? taper oui ou non".center(50)).upper()#accept oui/non
    tag = ["OUI", "NON"]
    while answer not in tag:#if input different =error
        print("ERREUR de saisie taper oui ou non".center(50))
        answer = input("Entrer votre réponce de nouveau".center(50)).upper()
    return answer
