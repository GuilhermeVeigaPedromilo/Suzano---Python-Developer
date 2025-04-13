saldo = 1011.00
saque = float(input("INFORME O VALOR DE SAQUE"))

if saldo >= saque:
    print("SAQUE REALIZADO, TOTAL: ", saque)
else:
    print("SALDO INSUFICIENTE")
    print("OPERAÇÃO CANCELADA")