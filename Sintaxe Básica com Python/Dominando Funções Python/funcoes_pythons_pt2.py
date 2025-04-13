#  marca = "Motorola"
#  modelo = "G5 s plus"
#  valor = 500
#  carregador = "Turbo Power"

#  Positional only
def criar_celular(marca, modelo, /, valor, carregador):
    print(marca, modelo, valor, carregador)

criar_celular("Motorola", "G5 s plus", valor=500, carregador="Turbo Power")
# Marca e modelo são positional only e após / são positional or keyword

# Objetos de primeira classe
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

# Escopo local e escopo global
salario = 1011

def salario_bonus(bonus):
    global salario
    reajuste = salario + bonus
    print(reajuste)

exibir_resultado(10, 10, somar)
salario_bonus(250)