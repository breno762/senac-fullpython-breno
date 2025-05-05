class Colaborador:
    def __init__(self, id, nome, cargo, salario):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Cargo: {self.cargo} | Salário: R${self.salario:.2f}"


class SistemaColaboradores:
    def __init__(self):
        self.colaboradores = {
            1: Colaborador(1, "Ana Souza", "Analista de Sistemas", 5200.00),
            2: Colaborador(2, "Bruno Lima", "Gerente de Projetos", 8500.00),
            3: Colaborador(3, "Carlos Pereira", "Técnico de Suporte", 3000.00),
            4: Colaborador(4, "Daniela Castro", "Desenvolvedora Backend", 6800.00),
            5: Colaborador(5, "Eduardo Almeida", "Designer UX/UI", 4700.00),
            6: Colaborador(6, "Fernanda Silva", "Coordenadora de RH", 7500.00),
        }

    def adicionar_colaborador(self, colaborador):
        if colaborador.id in self.colaboradores:
            print("❌ Já existe um colaborador com esse ID.")
        else:
            self.colaboradores[colaborador.id] = colaborador
            print("✅ Colaborador adicionado com sucesso.")

    def buscar_por_id(self, id):
        colaborador = self.colaboradores.get(id)
        if colaborador:
            print("\n🔍 Colaborador encontrado:")
            print(colaborador)
        else:
            print("❌ Colaborador não encontrado.")

    def listar_acima_salario(self, salario_minimo):
        print(f"\n💰 Colaboradores com salário acima de R${salario_minimo:.2f}:")
        encontrados = False
        for colab in self.colaboradores.values():
            if colab.salario > salario_minimo:
                print(colab)
                encontrados = True
        if not encontrados:
            print("Nenhum colaborador com salário acima desse valor.")

    def menu(self):
        while True:
            print("\n===== MENU =====")
            print("1 - Adicionar colaborador")
            print("2 - Buscar colaborador por ID")
            print("3 - Listar colaboradores com salário acima de X")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    id = int(input("ID: "))
                    nome = input("Nome: ")
                    cargo = input("Cargo: ")
                    salario = float(input("Salário: "))
                    colaborador = Colaborador(id, nome, cargo, salario)
                    self.adicionar_colaborador(colaborador)
                except ValueError:
                    print("❌ Entrada inválida. Verifique os dados e tente novamente.")

            elif opcao == "2":
                try:
                    id = int(input("Digite o ID do colaborador: "))
                    self.buscar_por_id(id)
                except ValueError:
                    print("❌ ID inválido.")

            elif opcao == "3":
                try:
                    salario = float(input("Digite o valor mínimo do salário: R$ "))
                    self.listar_acima_salario(salario)
                except ValueError:
                    print("❌ Valor inválido.")

            elif opcao == "0":
                print("Encerrando o programa...")
                break

            else:
                print("❌ Opção inválida. Tente novamente.")


# Execução do sistema
if __name__ == "__main__":
    sistema = SistemaColaboradores()
    sistema.menu()

