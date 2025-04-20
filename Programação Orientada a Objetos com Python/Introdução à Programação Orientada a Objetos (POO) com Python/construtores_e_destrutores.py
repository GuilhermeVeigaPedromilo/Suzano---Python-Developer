# __init__ = Método construtor de classe 
# __del__ = Método destrutor de classe
# Método construtor é chamado quando o objeto é instanciado
# Método destrutor é chamado quando o objeto é destruído

class Forno:
    def __init__(self, status=False, temp=0):
        self.status = status
        self.temp = temp
        
    def ligar(self):
        self.status = True
        print("Forno ligado")

    def desligar(self):
        self.status = False
        print("Forno desligado")

    def __del__(self):
        print("Forno destruído")

# Criando um objeto da classe Forno
forno = Forno(False, 120)
print(f"Status do forno: {forno.status}")
forno.ligar()
print(f"Status do forno: {forno.status}")
forno.desligar()
print(f"Status do forno: {forno.status}")

# O objeto forno será destruído quando sair do escopo
# Isso chamará o método __del__ automaticamente

forno_class = Forno()
del forno_class
print("Forno_class destruído")