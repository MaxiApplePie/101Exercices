# 023 ##################################
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
for k, v in employes.items():
    print(k, v)

print(sum([v for k, v in employes.items()]))

print(dir(employes))
print(sum(employes.values()))

# 024 ##################################
import random

nombre_aleatoire = random.randint(0, 5)
print(nombre_aleatoire)

# 025 ##################################
liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]

resultat = [i*(i+1%(i*5)) for i in sorted(list(set(liste)))]
# resultat = [i*2 for i in sorted(list(set(liste)))]
print(resultat)

# 026 ##################################
import constants
print(constants.nom)


# 027 ##################################
import os
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(__file__).join('images'))



# 022 ##################################

