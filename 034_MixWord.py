import random

mot = "Bonjour"
mylist = list(mot.lower())
random.shuffle(mylist)
print(''.join(mylist).capitalize())

# 035 ###############################################
nombre = 2938.48872
decimales = 3

print(f"Nombre tronqué: {nombre:.{decimales}f}")

# 036 ###############################################
a = 20
print('Vous êtes majeur !') if a == 20 else ''
