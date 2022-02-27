class Voiture():
	def __init__(self, marque: str, prix, couleur):
		self.marque = marque.capitalize()
		self.prix = prix
		self.couleur = couleur

	def __repr__(self):
		return f'Votre voiture est une {self.marque} {self.couleur} qui coute {self.prix}$'

super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture.marque)
print(super_voiture.prix)
print(super_voiture.couleur)
print(super_voiture)
