# Importation du module random
import random


# Définition des limites que peuvent atteindre le nombre avec une variable pour le refaire facilement.
# Les input sont les deux questions pour le minimum puis pour le maximum. L'output est le nombre aléatoire qui sera décidé
def borne():
    print(" \nDéfinition des limites que peut atteindre le chiffre à deviner. ")
    minimum = int(input("\nLe plus petit nombre (entier) peut être: "))
    maximum = int(input("\nLe plus grand nombre (entier) peut être: "))
    return random.randint(minimum, maximum)


nombre = borne()

jeu = True
essai = 0

# La boucle n'opèrera que si "jeu" est True, ce qui se fait tant que l'utilisateur dit oui à la possibilité de rejouer
while jeu == True:
    guess = int(input("\nÀ vous de deviner le nombre que j'ai choisi: "))

    # Félicitations à l'utilisteur lorsqu'il réussi
    if guess == nombre:
        essai += 1
        bravo = f"\nBravo, bonne réponse! Vous avez réussi en: {essai} essai(s)"
        print(bravo)
        encore = str(input("Voulez-vous rejouer? 'y' pour Oui et 'n' pour Non: "))
        if encore == "y" or encore == "Y":
            print("Recommençons!")
            nombre = borne()
            essai = 0
        else:
            print("Au revoir.")
            jeu = False

    # Indices à l'utilisateur pour l'aider à deviner le nombre
    else:
        if guess <= nombre:
            print("C'est plus!")
            essai += 1
        else:
            print("C'est moins!")
            essai += 1