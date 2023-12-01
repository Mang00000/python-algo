from random import *
from string import *

import os
os.system('cls')


run = True
nombre: int = randint(1,100)
guess_count: int = 0


def AskInt() -> int: 
    boucle2 = True
    while boucle2:
        check2: str = input("Ecrivez le nombre que vous voulez  ")
        if(check2.isnumeric()):
            boucle2 = False
        else:
            print("veuillez rentrer un nombre")
    return int(check2)
    


def check_int():
    boucle = True
    while boucle:
        try:
            check: int = int(input("Ecrivez le nombre que vous voulez  "))
            break
        except ValueError:
            print("veuillez rentrer un nombre")
    return check

            


while run:
    guess: int = AskInt()
    guess_count += 1
    if(guess == nombre):
        print(f'Bravo vous avez trouvé le nombre en {guess_count} essais')
        run = False
    elif(guess < nombre):
        print("C'est plus que ça !")
    else:
        print("C'est moins que ça !")