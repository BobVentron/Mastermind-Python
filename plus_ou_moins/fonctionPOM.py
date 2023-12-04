from random import randint

def numrandom(difficulter: int) -> int : 
    return randint(1, (difficulter*50))

def plus_ou_moins_nb(nbchercher : int, nbsaisi: int) -> str : 
    if nbchercher == nbsaisi :
        return f"Bingo vous avez trouver!!"
    elif nbsaisi > nbchercher : 
        return "Le nombre a trouver est plus petit!"
    elif nbsaisi < nbchercher :
        return "Le nombre a trouver est plus grand!"
    else:
        return "oula il y a un problème la!!"
    
def chiffre_bon(nbchercher : int, nbsaisi) -> bool : 
    return not (nbsaisi < 0 or nbchercher < nbsaisi)