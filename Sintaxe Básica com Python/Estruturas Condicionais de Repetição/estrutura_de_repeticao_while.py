saldo = 2000
extrato = [("Salário", 2000), ("Despesas", -1000), ("VIDA CAP", -1000)]

while True: # WHILE "INFINITO"
    print("\nESCOLHA UMA DAS OPÇÕES: ")
    print("[1] Sacar\n[2] Extrato\n[3] Sair")

    try:
        escolher_opcao = int(input("INSIRA SUA ESCOLHA: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue # Utilizado para pular o processo

    if escolher_opcao == 1:
        saque = float(input("INSIRA O VALOR A SACAR: "))
        if saque > saldo:
            print("VALOR INVÁLIDO: Saldo insuficiente.")
        else:
            saldo -= saque
            extrato.append(("Saque", -saque))
            print("VALOR SACADO COM SUCESSO")
    
    elif escolher_opcao == 2:
        print("\n===== EXTRATO =====")
        for desc, valor in extrato:
            print(f"{desc}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
    
    elif escolher_opcao == 3:
        print("Você saiu da sua conta")
        break
    
    else:
        print("Esta opção não existe.")