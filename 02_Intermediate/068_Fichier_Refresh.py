import os
import time

dossier = r'C:\Users\OMEN\Desktop'
dossier_a_trouver = 'Python'
chemin = os.path.join(dossier, dossier_a_trouver)

while True:
    if os.path.exists(chemin):
        print('Trouvé')
        break
    else:
        print('Dossier introuvable ...')
        time.sleep(3)
