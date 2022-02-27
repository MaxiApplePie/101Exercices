

class SuperStr(str):
    def __init__(self, parm):
        self.parm = parm

    def __add__(self, other):
        return SuperStr(f"{self.parm} {other}")

s = SuperStr('Bonjour')
print(s + 'tout' + 'le' + 'monde')

