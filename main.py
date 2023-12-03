from random import randint

def ramdomMastermind(color : list , difficulte : int) -> list : 
    listcolor = []
    while not difficulte == 0 :
        colorrandom = color[randint(1,len(color))-1]
        if colorrandom in listcolor : continue
        listcolor.append(colorrandom)
        difficulte -= 1
    return listcolor

def couleurCorect(couleurATrouver : list, listCouleur : list) -> int :
    nbCouleurBonne = 0
    for e in listCouleur :
        if e in couleurATrouver : 
            nbCouleurBonne += 1
    return nbCouleurBonne

def couleurBienPlacer (couleurATrouver : list, listcouleur : list) -> int :
    i = 0
    compt = 0
    while not i == len(couleurATrouver):
        if couleurATrouver[i] == listcouleur[i]:
            compt += 1
        i += 1
    return compt


def gestionMastermind():
    color = ["rouge", "vert", "bleu", "jaune"]
    difficulte = int(input("entrer le nombre de couleur que vous voulez trouver : "))
    if difficulte > len(color) :
        print("Erreur: la difficulter est trop élever pour le nombre de couleur choisi")
    else : 
        CouleurATrouver = ramdomMastermind(color, difficulte)
        print("Votre but est de retrouver la combinaisont de couleur générer :")
        print(CouleurATrouver)

        menu = """
            Entrer des couleurs (séparer par un espace) que vous penser être la solution,
            ou tapez sur "q" pour arrêter le jeu et avoir la solution.
        """
        while (choix := input(menu)) not in 'qQ' :
            listcouleur = choix.split()
            couleurBonne = True
            for e in listcouleur : 
                if e not in color: 
                    print("Vous avez saisi des couleurs érronner.")
                    couleurBonne = False
            
            if couleurBonne == True :
                if listcouleur == CouleurATrouver : 
                    print("Bravo vous avez trouver!!")
                    break
                else :
                    bienplacer = couleurBienPlacer(CouleurATrouver, listcouleur)
                    existe = couleurCorect(CouleurATrouver, listcouleur) - bienplacer
                    affichage = f'Vous n\'avez pas trouver la bonne combinaison. Voici quelque indice pour vous aider a la trouver: \n Il y a {bienplacer} pion bien placé \n Il y a {existe} pion qui existe dans la combinaison mais pas à la bonne place'
                    print(affichage)


        print("La solution était : ", end='')
        for e in CouleurATrouver : 
            print(e + " ", end='')

if __name__ == '__main__' :
    fini = False
    menu = """
        Tapez '1' pour commencer le jeu!
        Tapez '2' pour ...
        Taoez 'q' pour quitter.
        Votre choix : 
    """
    while (choix := input(menu)) not in 'qQ' :
        match choix : 
            case '1':
                gestionMastermind()
            case '2':
                print("Choix ")
            case _: 
                print("Choix non valide")