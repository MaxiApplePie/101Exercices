import os
import string


alphabet = string.ascii_uppercase
new_dir = 'alphabet'

current_place = os.path.dirname(__file__)
path_alphabet = os.path.join(current_place, new_dir)

try:
    os.mkdir(path_alphabet)
except:
    pass

for a in alphabet:
    path_alpha = os.path.join(path_alphabet, a)
    if not os.path.isdir(path_alpha):
        os.mkdir(path_alpha)


