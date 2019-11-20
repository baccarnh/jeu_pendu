from data import *
import random
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
    choice_pc = word()
    length_word = ""
    print("vous disposez de 8 essais pour deviner le ")
    for i in range(len(choice_pc)):
        length_word += "*"
    print(length_word)
    ofen = 1
    inter = ""
    for i in range(len(choice_pc)):
        inter += "*"
    while ofen < 9:
        print ('pour votre choix numero {} sur 8'.format(ofen))
        letters_found = compare(inter, choice_pc)
        print(letters_found)
        inter = letters_found
        ofen += 1








