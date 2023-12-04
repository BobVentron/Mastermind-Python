from plus_ou_moins import fonctionPOM as Plus_Ou_MoinsFonction

def gestionCliPlusOuMoins() -> None :
    """ Fonction de gestion du plus ou moins en mode CLI"""

    difficulte = int(input("entrer la difficulter que vous voulez (Elle doit être comrpise entre 1 et 20) : "))
    print(f"Vous devez trouver un nombre entre 0 et {difficulte*50}")
    nbchercher = Plus_Ou_MoinsFonction.numrandom(difficulte)
    print(f"Un peu de triche {nbchercher}")
    print("Votre but trouver le bon chiffre pour ca le jeu va vous dire si le chiffre a trouver est plus éléve ou mois élever que votre chiffre.")

    fin = False
    while not fin : 
        nombre = input("Entrer un chiffre que vous pensez être la solotion ou q pouu quitter : ")

        if nombre in "qQ": fin = True; continue
        if Plus_Ou_MoinsFonction.chiffre_bon(nbchercher, difficulte) : print("Erreur saisie"); continue
        if nombre == nbchercher : fin = True

        print(Plus_Ou_MoinsFonction.plus_ou_moins_nb(nbchercher, int(nombre)))

    print(f"Le nombre a trouver était {nbchercher}")