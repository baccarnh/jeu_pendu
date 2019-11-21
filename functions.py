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
    #num=0
    choice_player = letter()
    #num+=1
    #print ('pour votre choix numero {} sur 8'.format(num))
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

def level(player_list):

    player_name=presentation()
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
    #if choice_player not in choice_pc
        #ofen += 1
    #print(ofen)
    score = 0
    if ofen < 8: score += 8 - ofen
    print("le score du joueur {} sur cette partie est de {}".format(player_name, score))
    #arbitrator = {}
    #print(player_list)
    '''if player_name in player_list:'''
    #arbitrator[player_name] = arbitrator[player_name] + score
    '''else:
        arbitrator[player_name] = score'''
    player_list.append(player_name)

    level(player_list)
    print(player_list)
    return player_list
'''def liste(player_list):
    player_name=presentation()
    player_list.append(player_name)
    print(player_list)
    liste(player_list)
    return player_list'''


"""def record():
    arbitrator={}
    player_list=[]
    for cle in arbitrator
        player_list=player_list.append(cle)
    if player_name in player_list
        arbitrator[player_name]+=score
    else:
    arbitrator[playername]=score"""""










