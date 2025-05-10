class Conta:
    def __init__(self, saldo=0):
        self._saldo = 0
        self.saldo = saldo

    @property
    def saldo(self):
        return f"R${self._saldo:.2f}"

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Erro: saldo não pode ser negativo.")
        else:
            self._saldo = valor

# Exemplo de uso
conta = Conta(1000)
print(conta.saldo)

conta.saldo = -500
print(conta.saldo)
