import math

# Exo 007 ***************************************************
prenom = "Pierre"

# INSÉRER VOTRE CONDITION ICI.
# Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère. Ici c'est le cas,
if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")
# votre condition doit donc être vraie et printer la phrase "La variable est une chaîne de caractères".

prenom = 0

# INSÉRER VOTRE CONDITION DE NOUVEAU
# Cette fois-ci, la variable n'est pas égale à une chaîne de caractère. Votre condition doit donc être fausse et
if type(prenom) is str:
    print("La variable est une chaîne de caractères")
# la phrase ne doit pas s'afficher.

# Exo 008 ***************************************************
phrase = "Bonjour tout le monde."
nouvelle_phrase = phrase.replace('Bonjour', 'Bonsoir')

print(nouvelle_phrase)

# Exo 009 ***************************************************
chaine = "Pierre, Julien, Anne, Marie, Lucien"
prenoms = chaine.split(', ')
print(', '.join(sorted(prenoms)))

# Exo 010 ***************************************************
rayon = 10.0
volume = 4 * math.pi / 3 * pow(rayon, 3)

print(volume)