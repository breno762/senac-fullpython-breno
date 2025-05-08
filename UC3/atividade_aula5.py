class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"

class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario

    def __str__(self):
        return f"Livro: {self.livro.titulo} | Usuário: {self.usuario.nome}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def cadastrar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def cadastrar_usuario(self, nome, cpf):
        self.usuarios.append(Usuario(nome, cpf))

    def esta_emprestado(self, livro):
        return any(emp.livro.titulo.lower() == livro.titulo.lower() for emp in self.emprestimos)

    def cadastrar_emprestimo(self, titulo_livro, cpf_usuario):
        livro = next((l for l in self.livros if l.titulo.lower() == titulo_livro.lower()), None)
        usuario = next((u for u in self.usuarios if u.cpf == cpf_usuario), None)

        if not livro or not usuario:
            print(" Livro ou usuário não encontrado.")
            return

        if self.esta_emprestado(livro):
            print(f" O livro '{livro.titulo}' já está emprestado.")
            return

        self.emprestimos.append(Emprestimo(livro, usuario))
        print(f" Empréstimo registrado: {livro.titulo} para {usuario.nome}")

    def consultar_livros(self):
        print("\n Livros cadastrados:")
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)

    def consultar_usuarios(self):
        print("\n Usuários cadastrados:")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        for usuario in self.usuarios:
            print(usuario)

    def consultar_emprestimos(self):
        print("\n Empréstimos registrados:")
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
        for emprestimo in self.emprestimos:
            print(emprestimo)

    def exportar_dados(self, nome_arquivo="biblioteca_dados.txt"):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== LIVROS ===\n")
            for livro in self.livros:
                arquivo.write(str(livro) + "\n")

            arquivo.write("\n=== USUÁRIOS ===\n")
            for usuario in self.usuarios:
                arquivo.write(str(usuario) + "\n")

            arquivo.write("\n=== EMPRÉSTIMOS ===\n")
            for emprestimo in self.emprestimos:
                arquivo.write(str(emprestimo) + "\n")

        print(f"\nDados exportados com sucesso para '{nome_arquivo}'!")

def menu_biblioteca():
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro("Diário de Anne Frank", "Anne Frank")
    biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis")
    biblioteca.cadastrar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
    biblioteca.cadastrar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")
    biblioteca.cadastrar_livro("Coraline", "Neil Gaiman")
    biblioteca.cadastrar_livro("Memórias Póstumas de Brás Cubas", "Machado de Assis")
    biblioteca.cadastrar_livro("A Culpa é das Estrelas", "John Green")
    biblioteca.cadastrar_usuario("João Silva", "671.032.623-30")
    biblioteca.cadastrar_usuario("Maria Souza", "093.646.263-97")
    biblioteca.cadastrar_usuario("Ana Lima", "193.483.553-68")
    biblioteca.cadastrar_usuario("Pedro Oliveira", "088.835.463-00")
    biblioteca.cadastrar_usuario("Carla Mendes", "962.847.093-07")
    biblioteca.cadastrar_emprestimo("Diário de Anne Frank", "671.032.623-30")
    biblioteca.cadastrar_emprestimo("Dom Casmurro", "093.646.263-97")
    biblioteca.cadastrar_emprestimo("Harry Potter e a Pedra Filosofal", "193.483.553-68")

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Realizar empréstimo")
        print("4. Consultar livros")
        print("5. Consultar usuários")
        print("6. Consultar empréstimos")
        print("7. Exportar dados para .txt")
        print("0. Sair")
        print("8. Voltar")
        print("----------------------\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            biblioteca.cadastrar_livro(titulo, autor)
        elif opcao == "2":
            nome = input("Nome do usuário: ")
            cpf = input("CPF do usuário: ")
            biblioteca.cadastrar_usuario(nome, cpf)
        elif opcao == "3":
            titulo = input("Título do livro: ")
            cpf = input("CPF do usuário: ")
            biblioteca.cadastrar_emprestimo(titulo, cpf)
        elif opcao == "4":
            biblioteca.consultar_livros()
        elif opcao == "5":
            biblioteca.consultar_usuarios()
        elif opcao == "6":
            biblioteca.consultar_emprestimos()
        elif opcao == "7":
            biblioteca.exportar_dados()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        elif opcao == "8":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Acessar Biblioteca")
        print("0. Sair")
        print("----------------------\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_biblioteca()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

