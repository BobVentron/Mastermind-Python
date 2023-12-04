# -*- coding: utf-8 -*-

import Martermind.gestionCLI as gestionCliMastermind
import plus_ou_moins.gestionCLI as GestionCliPlusOuMoins

if __name__ == '__main__' :
    fini = False
    menu1 = """
        Tapez '1' pour commencer le jeu du Mastermind!
        Tapez '2' pour ...
        Taoez 'q' pour quitter.s
        Votre choix : 
    """
    menu2 = """
        Tapez '1' pour jouer au jeu en mode CLI.
        Tapez '2' pour jouer au jeu avec une interface graphique.
        Tapez 'q' pour quitter.
    """
    while (choix := input(menu1)) not in 'qQ' :
        match choix : 
            case '1':
                while (choix2 := input(menu2)) not in 'qQ' :
                    match choix2 : 
                        case '1':
                            gestionCliMastermind.gestionMastermindCLI()
                        case '2' :
                            print("La version avec interface graphique n'a pas encore été développer!")
                        case _ :
                            print("Choix non valide")
            case '2':
                while (choix2 := input(menu2)) not in 'qQ' :
                    match choix2 : 
                        case '1':
                            GestionCliPlusOuMoins.gestionCliPlusOuMoins()
                        case '2' :
                            print("La version avec interface graphique n'a pas encore été développer!")
                        case _ :
                            print("Choix non valide")
            case _: 
                print("Choix non valide")