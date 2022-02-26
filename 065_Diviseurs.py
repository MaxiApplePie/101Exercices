nombre = 50
# diviseurs = []

# for n in range(1, nombre + 1):
#     # print(nombre % n)
#     if nombre % n == 0:
#         diviseurs.append(n)

diviseurs = [n for n in range(1, nombre + 1) if nombre % n == 0]
print(diviseurs)