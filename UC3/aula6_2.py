from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Este é {self.nome}, um {self.__class__.__name__}.")

    @abstractmethod
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

    def correr(self):
        print(f"{self.nome} está correndo atrás da bola.")

    def abanar_rabo(self):
        print(f"{self.nome} está abanando o rabo.")
        
    def beber_agua(self):
        print(f"{self.nome} está bebendo água na tijela.")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

    def arranhar(self):
        print(f"{self.nome} está arranhando o sofá.")

    def pular(self):
        print(f"{self.nome} pulou na prateleira.")
        
    def beber(self):
        print(f"{self.nome} bebeu leite na tijela.")

c = Cachorro("Whisky")
g = Gato("Dori")

c.apresentar()
c.emitir_som()
c.correr()
c.abanar_rabo()
c.beber_agua()

print()

g.apresentar()
g.emitir_som()
g.arranhar()
g.pular()
g.beber()

