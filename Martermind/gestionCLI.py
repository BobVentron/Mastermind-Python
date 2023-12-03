# -*- coding: utf-8 -*-

from Martermind import fonctionM as MastermindFocntion

def gestionMastermindCLI():
    """ Fonction de gestion du Mastermind en mode CLI"""

    color = ["rouge", "vert", "bleu", "jaune"]
    difficulte = int(input("entrer le nombre de couleur que vous voulez trouver : "))
    if difficulte > len(color) :
        print("Erreur: la difficulter est trop élever pour le nombre de couleur choisi")
    else : 
        CouleurATrouver = MastermindFocntion.ramdomMastermind(color, difficulte)
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

            if not len(listcouleur) == len(CouleurATrouver):
                print(f"Il faut saisir {len(CouleurATrouver)} couleur!")
                couleurBonne = False
                
            if couleurBonne == True :
                if listcouleur == CouleurATrouver : 
                    print("Bravo vous avez trouver!!")
                    break
                else :
                    bienplacer = MastermindFocntion.couleurBienPlacer(CouleurATrouver, listcouleur)
                    existe = MastermindFocntion.couleurCorect(CouleurATrouver, listcouleur) - bienplacer
                    affichage = f'Vous n\'avez pas trouver la bonne combinaison. Voici quelque indice pour vous aider a la trouver: \n Il y a {bienplacer} pion bien placé \n Il y a {existe} pion qui existe dans la combinaison mais pas à la bonne place'
                    print(affichage)

        print("La solution était : ", end='')
        for e in CouleurATrouver : 
            print(e + " ", end='')
