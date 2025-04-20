import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class PessoaFisica:
    def __init__(self, nome: str, data_nascimento: datetime.date, cpf: str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao: 'Transacao'):
        self.transacoes.append(transacao)

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: 'Conta'):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
        self.data = datetime.datetime.now()
    
    def registrar(self, conta: 'Conta'):
        conta.saldo += self.valor
        return True

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
        self.data = datetime.datetime.now()
    
    def registrar(self, conta: 'Conta'):
        if isinstance(conta, ContaCorrente):
            if conta.limite_saques > 0 and conta.saldo >= self.valor:
                conta.saldo -= self.valor
                conta.limite_saques -= 1
                return True
        elif conta.saldo >= self.valor:
            conta.saldo -= self.valor
            return True
        return False

class Conta:
    contador = 0
    
    def __init__(self, cliente: 'Cliente', numero: int, agencia: str = "0001"):
        Conta.contador += 1
        self.numero = numero if numero else Conta.contador
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()
    
    def saldo(self) -> float:
        return self.saldo
    
    @classmethod
    def nova_conta(cls, cliente: 'Cliente', numero: int = None) -> 'Conta':
        return cls(cliente, numero)
    
    def sacar(self, valor: float) -> bool:
        transacao = Saque(valor)
        return transacao.registrar(self)
    
    def depositar(self, valor: float) -> bool:
        transacao = Deposito(valor)
        sucesso = transacao.registrar(self)
        if sucesso:
            self.historico.adicionar_transacao(transacao)
        return sucesso

class ContaCorrente(Conta):
    def __init__(self, cliente: 'Cliente', numero: int = None, agencia: str = "0001"):
        super().__init__(cliente, numero, agencia)
        self.limite = 250.0
        self.limite_saques = 5

class Cliente:
    def __init__(self, endereco: str, pessoa: PessoaFisica):
        self.endereco = endereco
        self.pessoa = pessoa
        self.contas: List[Conta] = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        return transacao.registrar(conta)
    
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class SistemaBancario:
    def __init__(self):
        self.clientes: Dict[str, Cliente] = {}
        self._iniciar_dados()
    
    def _iniciar_dados(self):
        # Adiciona um usuário inicial para testes
        pessoa = PessoaFisica("Gui", datetime.datetime.strptime("11/05/2007", "%d/%m/%Y").date(), "111.111.111-00")
        endereco = "Rua Curiuba - Jardim Del Rei - New Odissey/BA"
        cliente = Cliente(endereco, pessoa)
        self.clientes[pessoa.cpf] = cliente
        
        # Cria uma conta para o usuário inicial
        conta = ContaCorrente(cliente, 1)
        cliente.adicionar_conta(conta)
    
    def criar_usuario(self, nome: str, data_nascimento: str, cpf: str, 
                     logradouro: str, bairro: str, cidade: str, estado_sigla: str) -> bool:
        # Verifica se o CPF já existe
        if cpf in self.clientes:
            print("Dados inválidos: este CPF já está cadastrado no sistema.")
            return False
        
        # Conversão de data
        try:
            data_convertida = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de data inválido. Use o formato DD/MM/AAAA.")
            return False
        
        # Cria a pessoa física
        pessoa = PessoaFisica(nome, data_convertida, cpf)
        
        # Cria o endereço
        endereco = f"{logradouro} - {bairro} - {cidade}/{estado_sigla}"
        
        # Cria o cliente
        cliente = Cliente(endereco, pessoa)
        self.clientes[cpf] = cliente
        
        print(f"Dados cadastrados com sucesso, {nome}")
        return True
    
    def criar_conta(self, cpf: str, agencia: str = "0001") -> bool:
        cliente = self.clientes.get(cpf)
        if not cliente:
            print("Cliente não encontrado.")
            return False
        
        # Verifica o último número de conta existente
        ultimo_numero = 0
        for cliente_existente in self.clientes.values():
            for conta in cliente_existente.contas:
                if conta.numero > ultimo_numero:
                    ultimo_numero = conta.numero
        
        # Cria a nova conta
        nova_conta = ContaCorrente(cliente, ultimo_numero + 1, agencia)
        cliente.adicionar_conta(nova_conta)
        
        print(f"Conta Corrente criada para {cliente.pessoa.nome} com número {nova_conta.numero}")
        return True
    
    def autenticar(self, cpf: str) -> Optional[Cliente]:
        return self.clientes.get(cpf)
    
    def realizar_deposito(self, cliente: Cliente):
        if not cliente.contas:
            print("O cliente não possui contas cadastradas.")
            return
        
        # Selecionar conta
        conta_selecionada = self._selecionar_conta(cliente)
        if not conta_selecionada:
            return
        
        # Realizar depósito
        valor = float(input("\n======= DEPOSITAR =======\nDigite o valor do depósito: "))
        if valor <= 0:
            print("Valor inválido para depósito.")
            return
        
        if conta_selecionada.depositar(valor):
            print(f"Depósito de R${valor:.2f} realizado com sucesso na conta Nº {conta_selecionada.numero}.")
    
    def realizar_saque(self, cliente: Cliente):
        if not cliente.contas:
            print("O cliente não possui contas cadastradas.")
            return
        
        # Selecionar conta
        conta_selecionada = self._selecionar_conta(cliente)
        if not conta_selecionada:
            return
        
        # Verificar limites para conta corrente
        if isinstance(conta_selecionada, ContaCorrente):
            if conta_selecionada.limite_saques <= 0:
                print("Operação cancelada, você já atingiu o número de saques permitido")
                return
        
        # Realizar saque
        valor = float(input("\n======= SACAR =======\nDigite o valor do saque: "))
        if valor <= 0:
            print("Valor inválido para saque.")
            return
        
        if isinstance(conta_selecionada, ContaCorrente) and valor > conta_selecionada.limite:
            print(f"Operação cancelada, valor limite de saque é R${conta_selecionada.limite:.2f}")
            return
        
        if conta_selecionada.saldo < valor:
            print("Operação cancelada, valor de saque superior ao saldo")
            return
        
        if conta_selecionada.sacar(valor):
            transacao = Saque(valor)
            conta_selecionada.historico.adicionar_transacao(transacao)
            print(f"Saque realizado no valor de R$ {valor:.2f}")
    
    def exibir_extrato(self, cliente: Cliente):
        if not cliente.contas:
            print("O cliente não possui contas cadastradas.")
            return
        
        # Selecionar conta
        conta_selecionada = self._selecionar_conta(cliente)
        if not conta_selecionada:
            return
        
        print("\n======================= EXTRATO =======================")
        
        if not conta_selecionada.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in conta_selecionada.historico.transacoes:
                if isinstance(transacao, Deposito):
                    print(f"Depósito: +R${transacao.valor:.2f} -- {transacao.data}")
                elif isinstance(transacao, Saque):
                    print(f"Saque: -R${transacao.valor:.2f} -- {transacao.data}")
        
        print(f"\nSaldo: R$ {conta_selecionada.saldo:.2f}")
    
    def _selecionar_conta(self, cliente: Cliente) -> Optional[Conta]:
        if len(cliente.contas) == 1:
            return cliente.contas[0]
        
        print("\n====== SELECIONE A CONTA ======")
        for i, conta in enumerate(cliente.contas):
            print(f"[{i+1}] Conta Nº {conta.numero} - Agência {conta.agencia}")
        
        escolha = input("Escolha o número da conta: ")
        
        while not escolha.isdigit() or not (1 <= int(escolha) <= len(cliente.contas)):
            print("Escolha inválida. Tente novamente.")
            escolha = input("Escolha o número da conta: ")
        
        return cliente.contas[int(escolha) - 1]


class Menu:
    def __init__(self, sistema: SistemaBancario):
        self.sistema = sistema
        self.cliente_atual = None
    
    def exibir_menu_principal(self):
        print("""
================= BANCO PYTHON TECH =================

Escolha uma das opções abaixo para prosseguir =======>

[1] LOGIN
[2] CADASTRE-SE
[3] ENCERRAR OPERAÇÕES
""")
        return input("=> ")
    
    def exibir_menu_usuario(self):
        print(f"""
====================== BEM VINDO {self.cliente_atual.pessoa.nome.upper()} ======================

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] CRIAR CONTA CORRENTE
[5] SAIR

""")
        return input("=> ")
    
    def processar_login(self):
        print("\n================= BEM VINDO NOVAMENTE =================\n")
        cpf = input("INSIRA SEU CPF: ")
        
        cliente = self.sistema.autenticar(cpf)
        if cliente:
            self.cliente_atual = cliente
            print(f"Login feito com sucesso. Bem-vindo, {cliente.pessoa.nome}!")
            return True
        else:
            print("Não foi encontrado nenhum usuário com esse CPF")
            return False
    
    def processar_cadastro(self):
        print("\n=============== CADASTRE SUA CONTA AQUI ===============\n")
        
        nome = input("NOME COMPLETO: ")
        data_de_nascimento = input("DATA DE NASCIMENTO (DD/MM/AAAA): ")
        cpf = input("CPF: ")
        logradouro = input("LOGRADOURO: ")
        bairro = input("BAIRRO: ")
        cidade = input("CIDADE: ")
        estado_sigla = input("ESTADO (EX.: SP): ")
        
        if self.sistema.criar_usuario(nome, data_de_nascimento, cpf, logradouro, bairro, cidade, estado_sigla):
            self.sistema.criar_conta(cpf)
            return True
        return False
    
    def iniciar(self):
        while True:
            opcao = self.exibir_menu_principal()
            
            if opcao == "1":  # Login
                if self.processar_login():
                    self.menu_usuario()
            
            elif opcao == "2":  # Cadastrar
                self.processar_cadastro()
            
            elif opcao == "3":  # Sair
                print("Obrigado por utilizar o Banco Python Tech. Até logo!")
                break
            
            else:
                print("Opção inválida. Por favor, tente novamente.")
    
    def menu_usuario(self):
        while True:
            opcao = self.exibir_menu_usuario()
            
            if opcao == "1":  # Depositar
                self.sistema.realizar_deposito(self.cliente_atual)
            
            elif opcao == "2":  # Sacar
                self.sistema.realizar_saque(self.cliente_atual)
            
            elif opcao == "3":  # Extrato
                self.sistema.exibir_extrato(self.cliente_atual)
            
            elif opcao == "4":  # Criar Conta Corrente
                resposta = input("\n============ CRIAR UMA NOVA CONTA CORRENTE ============\n\nVocê deseja criar uma nova conta corrente (S/N)? ")
                if resposta.upper() in ["S", "SIM"]:
                    self.sistema.criar_conta(self.cliente_atual.pessoa.cpf)
            
            elif opcao == "5":  # Sair
                print("Desconectado com sucesso")
                self.cliente_atual = None
                break
            
            else:
                print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    sistema = SistemaBancario()
    menu = Menu(sistema)
    menu.iniciar()