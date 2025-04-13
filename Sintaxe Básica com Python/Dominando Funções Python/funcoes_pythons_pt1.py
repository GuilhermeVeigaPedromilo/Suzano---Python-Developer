# Funções com argumentos
def exibir_mensagem():
    print("Hello World!")

exibir_mensagem()

nome = input("INFORME SEU NOME: ")
recursos = f'''
[] Extrato
[] Saque
[] Investimentos'''

def exibir_mensagem_com_nome(nome):
    print(f"Olá, {nome}")

def exibir_recursos(recursos):
    print("Veja os recursos disponíveis: ", recursos)


# Args e kwargs, respectivamente tupla e dicionário (*args e **kwargs)
def exemplo_simples(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)


exibir_mensagem_com_nome(nome)
exibir_recursos(recursos)
exemplo_simples("Python", 3.10, True, linguagem="Python", versão="3.10", ativo=True)
# Quando há chaves e valores, será kwargs ou dicionário;