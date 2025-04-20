class Estudante:
    escola = "Escola de Programação"  # Variável de classe
    def __init__(self, nome, numero):
        self.nome = nome  # Variável de instância
        self.numero = numero  # Variável de instância


    def __str__(self) -> str:
        return f"Nome: {self.nome}, Número: {self.numero}, Escola: {Estudante.escola}"

def mostrar_informacoes(objs):
    for obj in objs:
        print(obj)

giorge = Estudante("George", 123)
Walter = Estudante("Walter", 456)

mostrar_informacoes([giorge, Walter])