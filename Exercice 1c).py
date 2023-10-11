nombre = 0
etoiles = f"***********"

# Print de la chaîne de caractères en enlevant une "*" à chauqe fois jusqu'à ce qu'il n'y ai plus rien
while nombre < 11:
    print(etoiles[nombre:])
    nombre += 1
