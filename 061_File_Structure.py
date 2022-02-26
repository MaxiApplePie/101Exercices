from os import path


def remonter_dossier(d: str, iterations: int):
    # Verifier que le chemin original exist
    if path.exists(d):
        for _ in range(iterations):
            d = path.dirname(d)
    else:
        raise IOError('Le chemin est invalide')
    return d


dossier = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\S49_PIP"
print(dossier)
print(remonter_dossier(dossier, 3))
