saldo = 500

def sacar(valor: float): # Início do bloco do método
    if saldo >= valor: # Início do bloco do if
        print("Saque realizado")
    # fim do bloco do if
print("Não foi possível sacar")
# Fim do bloco do método

sacar(100)