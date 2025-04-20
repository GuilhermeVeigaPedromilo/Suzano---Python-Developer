menu = """
============= SOLICITE A PIZZA =============

[1] SOLICITAR PIZZA
[2] STATUS DA PIZZA
[3] ENCERRAR OPERAÇÕES
===> """

menu_pizzas = """
============= ESCOLHA A PIZZA =============

[1] Calabresa
[2] Queijos
[3] Frango com Catupiry
[4] Portuguesa

==> """

menu_chef = """
========= LANCE O STATUS DA PIZZA =========

[1] ESTÁ SENDO PREPARADA
[2] ESTÁ COZINHANDO
[3] PRONTA
[4] SAIU PARA ENTREGA
[5] FOI ENTREGUE

==> """

menu_status = """
=========== VISUALIZE AS PIZZAS ===========
"""

class Pizza:
    def __init__(self, nome, ingredientes, valor, status="NÃO SOLICITADO"):
        self.nome = nome
        self.ingredientes = ingredientes
        self.status = status
        self.valor = valor

    def modify_status(self):
        self.status = int(input(menu_chef))

        if self.status == 1:
            print(f"STATUS: PIZZA - {self.nome} ESTÁ SENDO PREPARADA")
        
        elif self.status == 2:
            print(f"STATUS: PIZZA - {self.nome} ESTÁ COZINHANDO")

        elif self.status == 3:
            print(f"STATUS: PIZZA - {self.nome} PRONTA")
        
        elif self.status == 4:
            print(f"STATUS: PIZZA - {self.nome} SAIU PARA ENTREGA")

        elif self.status == 5:
            print(f"STATUS: PIZZA - {self.nome} FOI ENTREGUE")

        else:
            print("ERROR: FUNCTION NOT EXIST")

# Lista de pizzas disponíveis
pizzas_disponiveis = [
    Pizza("Calabresa", {"Calabresa", "Muçarela", "Massa"}, "R$ 50,00"),
    Pizza("Queijos", {"Cheddar", "Muçarela", "Massa"}, "R$ 50,00"),
    Pizza("Frango com Catupiry", {"Frango", "Catupiry", "Muçarela", "Massa"}, "R$ 55,00"),
    Pizza("Portuguesa", {"Presunto", "Ovo", "Cebola", "Muçarela", "Massa"}, "R$ 60,00")
]

while True:
    recursos = int(input(menu))

    if recursos == 1:
        escolha = int(input(menu_pizzas))
        
        if 1 <= escolha <= len(pizzas_disponiveis):
            pizza_escolhida = pizzas_disponiveis[escolha - 1]
            print(f"Você escolheu a pizza: {pizza_escolhida.nome} - {pizza_escolhida.valor}")
            pizza_escolhida.modify_status()
        else:
            print("ERROR: PIZZA NÃO EXISTE")

    elif recursos == 2:
        print(menu_status)
        for pizza in pizzas_disponiveis:
            print(f"Nome: {pizza.nome} - Status: {pizza.status} - Valor: {pizza.valor}")
        print("=========================================")
    
    elif recursos == 3:
        print("Encerrando operações...")
        break

    else:
        print("ERROR: FUNÇÃO NÃO EXISTE")