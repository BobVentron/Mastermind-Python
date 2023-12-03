# -*- coding: utf-8 -*-

from random import randint

def ramdomMastermind(color : list , difficulte : int) -> list : 
    """Permet de générer des couleur aléatoire pour le jeu du mastermin.
    Renvoie une list de couleur générer.
    Prend 2 paramétre qui sont : 
    Une liste de couleur 
    le nombre de couleur qui doit y avoir"""

    listcolor = []
    while not difficulte == 0 :
        colorrandom = color[randint(1,len(color))-1]
        if colorrandom in listcolor : continue
        listcolor.append(colorrandom)
        difficulte -= 1
    return listcolor

def couleurCorect(couleurATrouver : list, listCouleur : list) -> int :
    """Permet de savoir combien de couleur d'une liste sont présent dans une autre liste.
    Renvoie le nombre de couleur
    Prend 2 paramétre qui sont :
    2 liste du même type et de même longeur"""

    nbCouleurBonne = 0
    for e in listCouleur :
        if e in couleurATrouver : 
            nbCouleurBonne += 1
    return nbCouleurBonne

def couleurBienPlacer (couleurATrouver : list, listcouleur : list) -> int :
    """Permet de savoir combien de couleur d'une liste sont exactement a la même place dans une autre liste.
    Renvoie le nombre de couleur
    Prend 2 paramétre qui sont :
    2 liste du même type et de même longeur"""

    i = 0
    compt = 0
    while not i == len(couleurATrouver):
        if couleurATrouver[i] == listcouleur[i]:
            compt += 1
        i += 1
    return compt