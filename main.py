from random import randint

def ramdomMastermind(color : list , difficulte : int) -> list : 
    listcolor = []
    while not difficulte == 0 :
        colorrandom = color[randint(1,len(color))-1] 
        print(colorrandom)
        listcolor.append(colorrandom.join())
        difficulte -= 1
    return listcolor

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
                color = ["rouge", "vert", "bleu"]
                difficulte = int(input("entrer le nb de coulueu que vous voulez trouver : "))

                print(ramdomMastermind(color, difficulte))
            case '2':
                print("Choix ")
            case _: 
                print("Choix non valide")