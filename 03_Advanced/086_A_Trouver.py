from glob import glob


dossier = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython"
mot = 'QtWebEngine_ru'

doss = []
dossiers = glob(r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython/**", recursive=True)
for d in dossiers:
    if mot.lower() in d.lower():
        doss.append(d)
print(doss)