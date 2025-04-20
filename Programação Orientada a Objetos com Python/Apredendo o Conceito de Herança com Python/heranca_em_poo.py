# Herança Simples

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico de animal")

    def andar(self):
        print(f"{self.nome} está andando.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama o construtor da classe pai (Animal)
        self.raca = raca

    def fazer_som(self):
        print("Au au!")

    def latir(self):
        print("Woof woof!")

# Exemplo de Herança Simples
print("--- Herança Simples ---")
meu_cachorro = Cachorro("Rex", "Pastor Alemão")
print(f"Nome do cachorro: {meu_cachorro.nome}")
print(f"Raça do cachorro: {meu_cachorro.raca}")
meu_cachorro.fazer_som()
meu_cachorro.andar()
meu_cachorro.latir()

print("\n")

# Herança Múltipla

class Nadador:
    def nadar(self):
        print("Nadando...")

class Corredor:
    def correr(self):
        print("Correndo...")

class Triatleta(Nadador, Corredor):
    def __init__(self, nome):
        self.nome = nome

    def treinar(self):
        print(f"{self.nome} está treinando para o triatlo.")

# Exemplo de Herança Múltipla
print("--- Herança Múltipla ---")
meu_triatleta = Triatleta("Ana")
print(f"Nome do triatleta: {meu_triatleta.nome}")
meu_triatleta.nadar()
meu_triatleta.correr()
meu_triatleta.treinar()