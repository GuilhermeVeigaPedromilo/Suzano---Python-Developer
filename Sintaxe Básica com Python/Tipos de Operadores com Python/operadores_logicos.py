saldo = 1200
saque = str(input("INSIRA O VALOR DO SAQUE: "))
limite = 100

exp = saldo >= saque and saque <= limite
print(exp)
# OPERADOR AND OU E

exp_2 = saldo >= saque or saque <= limite
print(exp_2)
# OPERADOR OR OU OU

exp_3 = not saque > limite
print(exp_3)
# OPERADOR NOT OU NEGAÇÃO