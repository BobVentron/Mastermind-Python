from random import randint

def ramdomMastermind(color : list , difficulte : int) -> list : 
    listcolor = []
    while not difficulte == 0 :
        colorrandom = color[randint(1,len(color))-1]
        if colorrandom in listcolor : continue
        listcolor.append(colorrandom)
        difficulte -= 1
    return listcolor

def gestionMastermind():
    color = ["rouge", "vert", "bleu"]
    difficulte = int(input("entrer le nb de coulueu que vous voulez trouver : "))
    if difficulte > len(color) :
        print("Erreur: la difficulter est trop élever pour le nombre de couleur choisi")
    else : 
        CouleurATrouver = ramdomMastermind(color, difficulte)
        print("Votre but est de retrouver la combinaisont de couleur générer :")
        print(CouleurATrouver)

        menu = """
            Entrer des couleur (séparer par un espace) que vous penser être la solution,
            ou tapez sur "q" pour arrêter le jeu et avoir la solution.
        """
        while (choix := input(menu)) not in 'qQ' :
            listcouleur = choix.split()
            for e in listcouleur : 
                if e not in color: 
                    print("Vous avez saisi des couleurs érronner.")
            
            if listcouleur == CouleurATrouver : 
                print("Bravo vous avez trouver!!")
                break
            else :
                print("pas trouver")

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