import os.path
from pprint import pprint

fichier = "C:/Python36/python.exe"
ext = os.path.splitext(fichier)[1]
print(ext.strip('.'))

# print(os.environ['COMPUTERNAME'])
# print(os.environ['PYTHONPATH'])

pprint(list(os.environ.keys()))
