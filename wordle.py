import random
 
mots : list = []
with open("mots.txt", "r") as f:
    for line in f:
        mots.append(line.split("\n")[0].upper())
    f.close()
 
numbers = "1234567890"
 
def ask_str(message: str, lenght: int):
    run : bool = True
    while run:
        try_number : bool = True
        check: str = str(input(message)).strip().upper()
        if len(check) == lenght:
            for e in check:
                if e in numbers:
                    try_number = False
            if try_number:
                break
            else:
                print("veuillez rentrer une chaine de caractères svp")
        else:
            print(f'veuillez rentrer une chaine de {lenght} caractère')
 
    return check
 
 
 
def print_green(s : str):
        return f"\033[32;99m{s}\033[m"
 
def print_red(s : str):
        return f"\033[31;99m{s}\033[m"
 
def print_yellow(s : str):
        return f"\033[33;99m{s}\033[m"
 
def suppos_color(supposition_color, supposition):
    lst : list = []
    for i in range(len(supposition)):
        if supposition_color[i] == 0:
            lst.append(print_green(supposition[i]))
        if supposition_color[i] == 1:
            lst.append(print_yellow(supposition[i]))
        if supposition_color[i] == 2:
            lst.append(print_red(supposition[i]))
    return lst
 
 
 
 
def display_grid(grid : list):
    for line in grid:
        print(" ".join(line))
 
 
def random_word():
    return random.choice(mots)
 
def créer_dic(secret_word : str):
    dic : dict = {}
    for i in range(len(secret_word)):
        incremente_dic(dic, secret_word[i])
    return dic
 
 
def incremente_dic(dic : dict,key):
    try:
        dic[key] += 1
    except KeyError:
        dic[key] = 1
 
 
def play_wordle():
    tour : int = -1
    secret_word : str = random_word()
    grid : list = [["_" for _ in range(len(secret_word))] for _ in range(5)]
    run : bool = True
 
 
 
    print("Bienvenue sur le worlde !")
    print("Le mot à deviner contient", len(secret_word), "lettres.")
    display_grid(grid)
    print(secret_word)
 
 
 
    dic : dict = créer_dic(secret_word)
 
 
    while run:
        tour += 1
        if tour == 5:
            print("Désolé, vous avez épuisé toutes vos tentatives. Le mot était:", secret_word)
            exit()
 
        supposition = ask_str("Devinez une lettre ou le mot complet : ", len(secret_word))
 
 
        supposition_color = [2] * len(secret_word)
 
 
        if supposition == secret_word:
            print("Félicitations, vous avez deviné le mot ! Le mot était:", secret_word)
            run : bool = False
            break
        elif len(supposition) != len(secret_word):
            print(f"Veuillez entrer un mot de {len(secret_word)} lettres")
        else:
            for i in range(len(supposition)):
                if supposition[i] == secret_word[i]:
                    supposition_color[i] = 0
                    dic[supposition[i]] -= 1
                else:
                    supposition_color[i] = 2

                    
            for i in range(len(supposition)):
                if supposition[i] != 0:
                    if str(supposition[i]) in dic:
                        if dic[supposition[i]] > 0:
                            supposition_color[i] = 1
                        




                            """
                        #elif supposition[i] in secret_word:
                    if str(supposition[i]) in dic:
                        dic[supposition[i]] -= 1
                    if dic[supposition[i]] > 0:
                        supposition_color[i] = 1
                    else:
                        supposition_color[i] = 2
                        """


        
 
 
        grid[tour] = suppos_color(supposition_color, supposition)
        display_grid(grid)
        dic : dict = créer_dic(secret_word)

 
play_wordle()