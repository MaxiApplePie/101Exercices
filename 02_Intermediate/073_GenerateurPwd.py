import string
import random

# print(string.ascii_lowercase)
# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)
# print(dir(string))
string.ascii_uppercase

pwd = ''
pwd_list = list()
for _ in range(8):
    pwd_list.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
pwd = ''.join(pwd_list)

# Verifier le mot de passe
l_numbers = [x for x in pwd if x in string.digits]
l_upper = [x for x in pwd if x in string.ascii_uppercase]
print('Le mot de passe généré est {mdp} !'.format(mdp=pwd))
if len(pwd_list) >= 8:
    if any(l.isupper() for l in pwd):
        if len([n for n in pwd if n.isdigit()]) >= 2:
            print('Valide !')


