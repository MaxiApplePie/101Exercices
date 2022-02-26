
# 011 ##################################
a = 12
if a > 10 and str(a).isdigit():
    print('a est plus grand que 10')

# 012 ##################################
liste = list(range(5, 16))
print(liste)

# 013 ##################################
l = list(range(0, 101, 2))
print(l)


# 014 ##################################
import random
print(random.randint(0, 6))

# 015 ##################################
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
o_occurs = phrase.count(lettre_a_chercher)
print(o_occurs)

# 016 ##################################
ma_liste = ["Pierre", "Paul", "Marie"]
print(ma_liste[0])
print(ma_liste.index('Pierre'))
