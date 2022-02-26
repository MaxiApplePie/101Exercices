age = int(input('Entrez l\âge du chien: '))
if age < 0:
    print('Vous devez entrer un âge positif!')
else:
    if age <= 2:
        age_humain = age * 10.5
    else:
        age_humain = 21 + (age - 2) * 4
    print(age_humain)
