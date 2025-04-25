class Candidato:
    def __init__(self):
        """Inicializa a lista de notas"""
        self.notas = []

    def inserir_notas(self):
        """Solicita as notas ao usuário e valida as entradas"""
        for i in range(1, 5):
            while True:
                try:
                    nota = float(input(f"Informe a {i}ª nota (0 a 10): "))
                    if 0 <= nota <= 10:
                        self.notas.append(nota)
                        break
                    else:
                        print("A nota deve estar entre 0 e 10. Tente novamente.")
                except ValueError:
                    print("Valor inválido. Por favor, insira um número entre 0 e 10.")

    def calcular_media(self):
        """Calcula a média das notas"""
        return sum(self.notas) / len(self.notas)

    def verificar_status(self):
        """Verifica o status do candidato (Aprovado ou Reprovado)"""
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return f"Reprovado. Média insuficiente: {media:.2f}"

    def exibir_resultado(self):
        """Exibe a média das notas e o status do candidato"""
        media = self.calcular_media()
        status = self.verificar_status()
        print(f"\nNotas inseridas: {self.notas}")
        print(f"Média das notas: {media:.2f}")
        print(f"Status: {status}")

    def exibir_notas(self):
        """Exibe todas as notas inseridas pelo aluno"""
        print(f"Notas do aluno: {self.notas}")


aluno = Candidato()
aluno.inserir_notas()
aluno.exibir_resultado()
