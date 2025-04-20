# A classe é composta pelas as características e comportamentos

class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzz...")

# Objetos
cao_1 = Cachorro("Bruce", "Cinza e castanho", False)
cao_2 = Cachorro("Lili ", "Preta0")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)