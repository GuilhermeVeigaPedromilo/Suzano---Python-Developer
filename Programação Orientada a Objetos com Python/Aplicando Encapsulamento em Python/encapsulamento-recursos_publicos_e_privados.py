# Todo atributo privado é precedido por dois underscores (__), o que indica que ele não deve ser acessado diretamente fora da classe.
class Conta:
    def __init__(self, saldo=0):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso!")
        else:
            print("Valor inválido para saque.")

    def obter_saldo(self):
        return self.__saldo
    
# Exemplo de uso
conta = Conta(1000)
conta.depositar(500)
conta.sacar(200)
print(f"Saldo atual: {conta.obter_saldo()}")