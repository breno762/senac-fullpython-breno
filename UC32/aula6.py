from datetime import datetime

class Conta:
    def __init__(self, saldo_inicial=0):
        self._saldo = 0
        self._historico = []
        self.saldo = saldo_inicial
        self._registrar("Abertura da conta", self._saldo)

    @property
    def saldo(self):
        return f"R${self._saldo:.2f}"

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor
        self._registrar("Depósito", valor)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self._saldo -= valor
        self._registrar("Saque", valor)

    def _registrar(self, operacao, valor):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self._historico.append(f"[{timestamp}] {operacao}: R${valor:.2f}")

    def extrato(self):
        print("=== Extrato da Conta ===")
        for linha in self._historico:
            print(linha)
        print(f"Saldo atual: {self.saldo}")

    def salvar_extrato(self, nome_arquivo="extrato.txt"):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Extrato da Conta ===\n")
            for linha in self._historico:
                arquivo.write(f"{linha}\n")
            arquivo.write(f"Saldo atual: {self.saldo}\n")
        print(f"Extrato salvo em '{nome_arquivo}'")

if __name__ == "__main__":
    conta = Conta(100)        
    conta.depositar(50)          
    conta.sacar(30)              
    conta.extrato()              
    conta.salvar_extrato()       



