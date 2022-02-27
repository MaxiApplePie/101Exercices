class CustomListe(list):
    def __init__(self, *args):
        self.valeurs = list(args)


    def append(self, value):
        self.valeurs.append(value)











ma_liste = CustomListe('Pierre', 'Julien', 'Marie')

ma_liste.append('Bob')
ma_liste.append('Pierre')
print(ma_liste)
