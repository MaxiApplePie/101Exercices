import os

dir = os.path.dirname(__file__)
file_name = os.path.join(dir, '../01_Beginner/fichier.txt')

with open(file_name, 'w') as f:
    f.write('Bonjour')

