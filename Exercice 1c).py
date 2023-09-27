# Variable que nous allons va pouvoir modifier pour choisir jusqu'à quelle position nous allons print
nombre = 0
# Variable de la chaîne de caractères pour être capable de la modifier dans la boucle while
etoiles = f"***********"

# Print de la chaîne de caractères en enlevant une "*" à chauqe fois jusqu'à ce qu'il n'y ai plus rien
while nombre < 11:
    print(etoiles[nombre:])
    nombre += 1
