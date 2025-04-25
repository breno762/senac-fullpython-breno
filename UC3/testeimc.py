class IMC:
    def __init__(self, peso, altura):

        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser valores positivos.")
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

    def exibir_resultado(self):
        imc = self.calcular_imc()
        classificacao = self.classificar_imc()
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")

try:
    pessoa = IMC(70, 1.75)
    pessoa.exibir_resultado()
except ValueError as e:
    print(e)