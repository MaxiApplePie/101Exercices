from glob import glob


dossier = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython"

dossiers = glob(r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython/**")
print(len(dossiers))