# 017 ##################################

ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste[-1])
print(ma_liste[0:2])
print(ma_liste[1:3])

# 018 ##################################
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ma_liste[::2])

# 019 ##################################
ma_liste = [1, 2, 3]
ma_liste.extend([4, 5, 6])
print(ma_liste)

# 020 ##################################
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
set_01 = set(liste_01)
set_02 = set(liste_02)
print(set_01.intersection(set_02))

# 021 ##################################
liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
# Trier la liste ici
liste.sort(key=lambda x: x[1])
print(liste)

# 022 ##################################
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get('prenom'))
print(employes.get('01').get('identite').get('prenom'))
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))
