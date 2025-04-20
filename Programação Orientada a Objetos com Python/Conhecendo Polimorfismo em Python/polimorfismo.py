class Ave:
    def voar(self):
        print("Voar....")

class Pardal(Ave):
    def voar(self):
        print("Pardal voando baixo...")
        super().voar()

class Falcao(Ave):
    def voar(self):
        print("Falcão voando alto...")
        super().voar()

def fazer_voar(ave):
    ave.voar()
    print("A ave voou!")

a1 = Pardal()
a2 = Falcao()

fazer_voar(a1)
fazer_voar(a2)