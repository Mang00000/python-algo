# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:09:23 2023

@author: remsm
"""

from random import *
 
def ask_int(message: str, min: int, max: int):
    boucle = True
    while boucle:
        try:
            check: int = int(input(message))
            if min <= check <= max :
                break
            else:
                print(f'veuillez rentrer un nombre entre {min} et {max}')
        except ValueError:
            print("veuillez rentrer un nombre valide")
    return check
 
 
 
 
def computer_choice():
    n = randint(0, 2)
    return n
 
choix = ["pierre", "papier", "ciseaux"]
 
 
 
resultats = [
    ["égalité", "perdu", "gagné"],
    ["gagné", "égalité", "perdu"],
    ["perdu", "gagné", "égalité"]
    ]
 
while True:
    a = ask_int("-----------------choix-----------------\npierre(0)\npapier(1)\nciseaux(2)\n-----------------votre choix:-----------------\n", 0, 2)
    b = computer_choice()
    print(f'votre choix : {choix[a]}')
    print(f'choix ordinateur : {choix[b]}')
    print(resultats[a][b])
 
    replay = input("Voulez-vous refaire une partie ? (oui/non): ")
    if replay.lower() != "oui":
        print("-----------------fin de partie !-----------------")
        break
 