# Métodos de classe = cls
# Métodos de instância = self
# Métodos estáticos = Não tem acesso a classe ou instância

class Funcionrio:
    funcionarios = []  # Class-level attribute to store all employees

    def __init__(self, nome, num_cracha):
        self.nome = nome
        self.num_cracha = num_cracha

    @classmethod
    def criar_funcionario(cls, nome, num_cracha=None):
        if not cls.funcionarios:  # Check if the list is empty
            num_cracha = 1  # Start with 1 if no employees exist
        else:
            num_cracha = max(func.num_cracha for func in cls.funcionarios) + 1  # Increment the highest number
        novo_funcionario = cls(nome, num_cracha)
        cls.funcionarios.append(novo_funcionario)  # Add the new employee to the list
        return novo_funcionario
    
    @staticmethod
    def classificar_empresa():
        length = len(Funcionrio.funcionarios)
        if length < 10:
            return "Pequena"
        elif length < 50:
            return "Média"
        else:
            return "Grande"

# Create employees
func1 = Funcionrio.criar_funcionario("George")
func2 = Funcionrio.criar_funcionario("Walter")

# Print employee details
for func in Funcionrio.funcionarios:
    print(f"Nome: {func.nome}, Número do Cracha: {func.num_cracha}")

print("Classificação da empresa:", Funcionrio.classificar_empresa())