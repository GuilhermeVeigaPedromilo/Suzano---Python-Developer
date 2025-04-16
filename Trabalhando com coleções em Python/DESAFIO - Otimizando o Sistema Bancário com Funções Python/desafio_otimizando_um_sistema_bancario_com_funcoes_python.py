import datetime

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# Base de dados
users = [] # Lista de dicionários: {"nome": "gui", "data_de_nascimento": "11/05/2007", "cpf": "111.111.111.-11", "endereco": "logradouro - bairro - cidade/estado"}

conta_corrente = [] # {"gui" : {"agencia": 0001, "num_da_conta": 1}} - número da conta é sequencial (1, 2, 3, 4) e agência fixa

# Funções

def Create_User(nome, data_de_nascimento, cpf, logradouro, bairro, cidade, estado_sigla):
    # Verifica se o CPF já existe na lista de usuários
    for user in users:
        if user["cpf"] == cpf:
            print("Dados inválidos: este CPF já está cadastrado no sistema.")
            return False

    # Conversão de data
    data_convertida = datetime.datetime.strptime(data_de_nascimento, "%d/%m/%Y").date()

    novo_usuario = {
        "nome": nome,
        "data_de_nascimento": data_convertida,
        "cpf": cpf,
        "endereco": f"{logradouro} - {bairro} - {cidade}/{estado_sigla}"
    }

    users.append(novo_usuario)
    print(f"Dados cadastrados com sucesso, {nome}")
    return True

conta_corrente = []  # Lista de contas

def Create_Account(agencia, nome):
    # Verifica o último número de conta existente
    if len(conta_corrente) == 0:
        novo_num_conta = 1
    else:
        # Percorre todas as contas e pega o maior número de conta já criado
        ultimos_numeros = [list(conta.values())[0]["num_conta"] for conta in conta_corrente]
        novo_num_conta = max(ultimos_numeros) + 1

    nova_conta = {
        nome: {
            "agencia": agencia,
            "num_conta": novo_num_conta,
            "limite": 250,
            "num_saques": 0,
            "num_saques_limite": 5,
            "extrato": ""
        }
    }

    conta_corrente.append(nova_conta)
    print(f"Conta Corrente criada para {nome} com número {novo_num_conta}")
    return True

menu = """
================= BANCO PYTHON TECH =================

Escolha uma das opções abaixo para prosseguir =======>

[1] LOGIN
[2] CADASTRE-SE
[3] ENCERRAR OPERAÇÕES

=> """

cabecalho_login = """
================= BEM VINDO NOVAMENTE =================

"""

cabecalho_cadastro = """
=============== CADASTRE SUA CONTA AQUI ===============

"""

menu_user = """
====================== BEM VINDO ======================

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] SAIR

=> """

while True:
    opcoes_de_acesso = int(input(menu))

    if opcoes_de_acesso == 1:
        
        print(cabecalho_login)
        
        cpf_login = input("INSIRA SEU CPF: ")
        search_an_user = None
        for user in users:
            if user["cpf"] == cpf_login:
                search_an_user = user
                break

        if search_an_user:
            print("Login feito com sucesso")
            while True:
                opcoes_de_recursos = int(input(menu_user))

                if opcoes_de_recursos == 4:
                    print("Desconectado com sucesso")
                    break
        else:
            print("Não foi encontrado nenhum usuário com esse CPF")
    elif opcoes_de_acesso == 2:

        print(cabecalho_cadastro)

        nome = input("NOME COMPLETO: ")
        data_de_nascimento = input("DATA DE NASCIMENTO: ")
        cpf = input("CPF: ")
        logradouro = input("LOGRADOURO: ")
        bairro = input("BAIRRO: ")
        cidade = input("CIDADE: ")
        estado_sigla = input("ESTADO (EX.: SP): ")

        CADASTRO = Create_User(nome, data_de_nascimento, cpf, logradouro, bairro, cidade, estado_sigla)

        if CADASTRO == True:
            CONTA_CORRENTE = Create_Account("0001", nome)
            if CONTA_CORRENTE == True:
                print(users)
                print(conta_corrente)
    elif opcoes_de_acesso == 3:
        print("bye")
        break
    else:
        print("ERROR: PAGE NOT FOUND")
    

# while True:

#     opcao = input(menu)

#     if opcao == "1":
#         valor = float(input("Informe o valor do depósito: "))

#         if valor > 0:
#             saldo += valor
#             extrato += f"Depósito: R$ {valor:.2f}\n"

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "2":
#         valor = float(input("Informe o valor do saque: "))

#         excedeu_saldo = valor > saldo

#         excedeu_limite = valor > limite

#         excedeu_saques = numero_saques >= LIMITE_SAQUES

#         if excedeu_saldo:
#             print("Operação falhou! Você não tem saldo suficiente.")

#         elif excedeu_limite:
#             print("Operação falhou! O valor do saque excede o limite.")

#         elif excedeu_saques:
#             print("Operação falhou! Número máximo de saques excedido.")

#         elif valor > 0:
#             saldo -= valor
#             extrato += f"Saque: R$ {valor:.2f}\n"
#             numero_saques += 1

#         else:
#             print("Operação falhou! O valor informado é inválido.")

#     elif opcao == "3":
#         print("\n================ EXTRATO ================")
#         print("Não foram realizadas movimentações." if not extrato else extrato)
#         print(f"\nSaldo: R$ {saldo:.2f}")
#         print("==========================================")

#     elif opcao == "4":
#         print("Você foi desconectado com sucesso!!!")
#         break

#     else:
#         print("Operação inválida, por favor selecione novamente a operação desejada.")