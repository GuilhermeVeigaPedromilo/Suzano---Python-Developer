import datetime

# Base de dados
users = [
    {'nome': 'Gui', 'data_de_nascimento': datetime.date(2007, 5, 11), 'cpf': '111.111.111-00', 'endereco': 'Rua Curiuba - Jardim Del Rei - New Odissey/BA'}
] # Lista de dicionários: {"nome": "gui", "data_de_nascimento": "11/05/2007", "cpf": "111.111.111.-11", "endereco": "logradouro - bairro - cidade/estado"}

conta_corrente = [
    {"111.111.111-00": {
        'agencia': '0001',
        'limite': 250,
        'num_conta': 1,
        'num_saques': 0,
        'num_saques_limite': 5,
        'extrato': '',
        'saldo': 0
    }}
] # {"gui" : {"agencia": 0001, "num_da_conta": 1}} - número da conta é sequencial (1, 2, 3, 4) e agência fixa

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


def Create_Account(agencia, nome, cpf):
    # Verifica o último número de conta existente
    if len(conta_corrente) == 0:
        novo_num_conta = 1
    else:
        # Percorre todas as contas e pega o maior número de conta já criado
        ultimos_numeros = [list(conta.values())[0]["num_conta"] for conta in conta_corrente]
        novo_num_conta = max(ultimos_numeros) + 1

    nova_conta = {
        cpf : {
            "agencia": agencia,
            "limite": 250,
            "num_conta": novo_num_conta,
            "num_saques": 0,
            "num_saques_limite": 5,
            "extrato": "",
            "saldo": 0
        }
    }

    conta_corrente.append(nova_conta)
    print(f"Conta Corrente criada para {nome} com número {novo_num_conta}")
    return True

def Depositar(cpf, valor):
    contas_do_cpf = [conta for conta in conta_corrente if cpf in conta]

    if len(contas_do_cpf) > 1:
        print("\n====== SELECIONE A CONTA PARA DEPÓSITO ======")
        for i, conta in enumerate(contas_do_cpf):
            info = conta[cpf]
            print(f"[{i+1}] Conta Nº {info['num_conta']} - Agência {info['agencia']}")

        escolha = input("Escolha o número da conta: ")

        while not escolha.isdigit() or not (1 <= int(escolha) <= len(contas_do_cpf)):
            print("Escolha inválida. Tente novamente.")
            escolha = input("Escolha o número da conta: ")

        conta_selecionada = contas_do_cpf[int(escolha) - 1][cpf]
    else:
        conta_selecionada = contas_do_cpf[0][cpf]

    horario = datetime.datetime.now()
    conta_selecionada["saldo"] += valor
    conta_selecionada["extrato"] += f"Depósito: +R${valor:.2f} -- {horario}\n"
    print(f"Depósito de R${valor:.2f} realizado com sucesso na conta Nº {conta_selecionada['num_conta']}.")
    return True
    

def Extrato(cpf):
    contas_do_cpf = [conta for conta in conta_corrente if cpf in conta]

    if len(contas_do_cpf) > 1:
        print("\n===== SELECIONE A CONTA PARA VER O EXTRATO =====")
        for i, conta in enumerate(contas_do_cpf):
            info = conta[cpf]
            print(f"[{i+1}] Conta Nº {info['num_conta']} - Agência {info['agencia']}")

        escolha = input("Escolha o número da conta: ")

        while not escolha.isdigit() or not (1 <= int(escolha) <= len(contas_do_cpf)):
            print("Escolha inválida. Tente novamente.")
            escolha = input("Escolha o número da conta: ")

        conta_selecionada = contas_do_cpf[int(escolha) - 1][cpf]
    else:
        conta_selecionada = contas_do_cpf[0][cpf]

    extrato = conta_selecionada["extrato"]
    saldo = conta_selecionada["saldo"]

    print(menu_extrato)
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

def Sacar(cpf, valor):
    contas_do_cpf = [conta for conta in conta_corrente if cpf in conta]

    if len(contas_do_cpf) > 1:
        print("\n===== SELECIONE A CONTA PARA EFETUAR SAQUE =====")
        for i, conta in enumerate(contas_do_cpf):
            info = conta[cpf]
            print(f"[{i+1}] Conta Nº {info['num_conta']} - Agência {info['agencia']}")

        escolha = input("Escolha o número da conta: ")

        while not escolha.isdigit() or not (1 <= int(escolha) <= len(contas_do_cpf)):
            print("Escolha inválida. Tente novamente.")
            escolha = input("Escolha o número da conta: ")

        conta_selecionada = contas_do_cpf[int(escolha) - 1][cpf]
    else:
        conta_selecionada = contas_do_cpf[0][cpf]
    
    verify_num_saques_limite = conta_selecionada["num_saques_limite"]
    verify_num_de_saques = conta_selecionada["num_saques"]
    verify_limite = conta_selecionada["limite"]

    if valor > verify_limite:
        print(f"Operação cancelada, valor limite de saque é R${verify_limite:.2f}")
    else:
        if verify_num_de_saques < verify_num_saques_limite:
            if valor < conta_selecionada["saldo"]:
                horario = datetime.datetime.now()
                conta_selecionada["num_saques"] += 1
                conta_selecionada["saldo"] -= valor
                conta_selecionada["extrato"] += f"Saque: -R${valor:.2f} -- {horario}\n"
                print(f"Saque realizado no valor de R$ {valor:.2f}")
            else:
                print("Operação cancelada, valor de saque superior ao saldo")
        else:
            print("Operação cancelada, você já atingiu o número de saques permitido")


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
[4] CRIAR CONTA CORRENTE
[5] SAIR

=> """

menu_criar_conta = """
============ CRIAR UMA NOVA CONTA CORRENTE ============

Você deseja criar uma nova conta corrente (S/N) ? """
menu_deposito = """
============ DEPOSITE O VALOR NA SUA CONTA ============

=> """

menu_extrato = """
======================= EXTRATO =======================
"""

menu_sacar ="""
======================= SACAR =========================

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

                if opcoes_de_recursos == 1:
                    valor_de_deposito = float(input(menu_deposito))
                    Depositar(search_an_user["cpf"], valor_de_deposito)

                elif opcoes_de_recursos == 2:
                    valor_de_saque = float(input(menu_sacar))
                    Sacar(search_an_user["cpf"], valor_de_saque)

                elif opcoes_de_recursos == 3:
                    print(menu_extrato)
                    Extrato(search_an_user["cpf"])

                elif opcoes_de_recursos == 4:
                    criar_conta_opcoes = str(input(menu_criar_conta))

                    if criar_conta_opcoes == "S" or "s":
                        Create_Account("0001", search_an_user["nome"], search_an_user["cpf"])
                    
                elif opcoes_de_recursos == 5:
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
            CONTA_CORRENTE = Create_Account("0001", nome, cpf)
    elif opcoes_de_acesso == 3:
        print("bye")
        break
    else:
        print("ERROR: PAGE NOT FOUND")