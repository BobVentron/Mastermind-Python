from random import randint

def numrandom(difficulter: int) -> int : 
    """Fontion qui génére un nombre random pour le plus ou moins. Renvoie un int.
    Prend 1 paramètre qui est la difficulter voulue par le joueur"""

    return randint(1, (difficulter*50))

def plus_ou_moins_nb(nbchercher : int, nbsaisi: int) -> str : 
    """Fonction qui renvoie si on a trouver le nombre ou si le nombre saisi est plus ou moins grand.
    Renvoie un str. 
    Prend 2 paramètre : 
    le bombre a trouver (en int)
    le nombre saisi pas le joueur (en int)"""

    if nbchercher == nbsaisi :
        return f"Bingo vous avez trouver!!"
    elif nbsaisi > nbchercher : 
        return "Le nombre a trouver est plus petit!"
    elif nbsaisi < nbchercher :
        return "Le nombre a trouver est plus grand!"
    else:
        return "oula il y a un problème la!!"
    
def chiffre_bon(difficulter : int, nbsaisi : int) -> bool : 
    """Fonction qui renvoie si le nombre saisi pas le joeur est bien dans le bonne intervale. 
    Renvoie un booléen.
    Prend 2 parametre: 
    la difficulter (en int)
    le nombre saisi par le joueur (en int)"""

    return (nbsaisi < 0 or (difficulter*50) < nbsaisi)