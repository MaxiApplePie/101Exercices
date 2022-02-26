from datetime import datetime
startTime = datetime.now()

_ = [i*2 for i in range(999999)]

print(datetime.now() - startTime)


prenom = "Pierre"
nom = "Dupont"
print(f"Bonjour je m'appelle {prenom} {nom}")

import string

mot = "Udemy"
print(type(mot[::-1]))
print(mot[::-1].capitalize())


