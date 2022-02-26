import string

digits = string.digits


def isdigit(nombre):
    if not isinstance(nombre, str):
        print('Saisir des nombres !')
    else:
        no_digits = [x for x in nombre if x not in digits]
        if len(no_digits) == 0:
            return True
    return False


print(isdigit("18542444"))
