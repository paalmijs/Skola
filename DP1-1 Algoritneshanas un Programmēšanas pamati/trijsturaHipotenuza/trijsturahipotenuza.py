#Importēt math bibliotēku
import math

# Pieprasīt vajadzīgos parametrus
katete1 = float(input("Ievadiet 1. katetes garumu: "))
katete2 = float(input("Ievadiet 2. katetes garumu: "))

#Apreiķināt hipotenūzas garumu izmantojot Pitagora teoremu
hipotenuza = math.sqrt(katete1**2 + katete2**2)

#Izdot rezūltātu
print(f"Hipotenuzas garums ir: ", hipotenuza)
