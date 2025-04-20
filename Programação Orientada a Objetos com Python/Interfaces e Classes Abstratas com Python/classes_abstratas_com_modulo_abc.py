from abc import ABC, abstractmethod, abstractproperty
# O módulo abc fornece as ferramentas para definir classes abstratas em Python.
# Uma classe abstrata é uma classe que não pode ser instanciada diretamente e pode conter métodos abstratos, que são métodos sem implementação.
# Classes abstratas são úteis quando você deseja definir uma interface comum para um grupo de subclasses, forçando-as a implementar certos métodos.

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractproperty
    def marca(self):
        pass

#  As classes filhas devem implementar os métodos abstratos definidos na classe pai.
#  Se não o fizerem, elas também se tornam classes abstratas e não podem ser instanciadas.
#  Além disso, é possível forçar propiedades abstratas, que são atributos que devem ser implementados nas subclasses.

# class ControleArCondicionado(ControleRemoto):
#     def desligar(self):
#         print("Desligando o ar condicionado...")

# class ControleTV(ControleRemoto):
#     def ligar(self):
#         print("Ligando a TV...")

class ControleArCondicionado(ControleRemoto):
    def marca(self):
        return "Ps Br"
    def ligar(self):
        print("Ligando o ar condicionado...")
    def desligar(self):
        print("Desligando o ar condicionado...")

class ControleTV(ControleRemoto):
    def marca(self):
        return "Good Eletric"
    def ligar(self):
        print("Ligando a TV...")
    def desligar(self):
        print("Desligando a TV...")
    
controlePsBr = ControleArCondicionado()
controleGoodEletric = ControleTV()
controlePsBr.desligar()
controleGoodEletric.ligar()