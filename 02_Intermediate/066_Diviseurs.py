nombre = 1000
# diviseurs = []

# for n in range(1, nombre + 1):
#     # print(nombre % n)
#     if nombre % n == 0:
#         diviseurs.append(n)

diviseurs = [n for n in range(1, nombre + 1) if (n % 7 == 0 and n % 3 != 0)]
print(diviseurs)