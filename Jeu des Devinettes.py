#Définition des bornes
print("Définition des limites que peut atteindre le chiffre à deviner. \n")
petit = int(input("Le plus petit nombre (entier) peut être: \n"))
grand = int(input("Le plus grand nombre (entier peut être: \n" ))


#Importation du module random
import random
nombre = random.randint(petit, grand)

#Définition de la variable pour compter le nombre d'essais
essai = 1

guess = int(input("Que pensez-vous être le nombre (entier): \n"))

if guess == nombre:
    reussite = True
    bravo = f"Vous avez réussi! Nombre d'essais: {essai}"
    print(bravo)

else:
    reussite = False


while reussite == False:
    if guess <= nombre:
        print("C'est plus!")
        guess
        essai += 1
    elif guess >= nombre:
        print("C'est moins!")
        guess
        essai += 1
    else:
        print("Ce n'est pas un nombre entier, recommencez")
        guess
        essai += 1