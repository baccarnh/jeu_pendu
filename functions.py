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

def compare():
    result=""
    choice_pc=word()
    print (choice_pc)
    choice_player=letter()
    
    for i in range(len(choice_pc)):
        if choice_pc[i] == choice_player:
            result=result+choice_player
        else:
            result=result+'*'
    return result



presentation()

print(compare())






