class UsuarioRepository:
    def __init__(self, arquivo='usuarios.txt'):
        self.usuarios = []
        self.arquivo = arquivo
        self.carregar_do_arquivo()

    def carregar_do_arquivo(self):
        try:
            with open(self.arquivo, 'r') as f:
                for linha in f:
                    nome, email = linha.strip().split(',')
                    self.usuarios.append({'nome': nome, 'email': email})
        except FileNotFoundError:
            pass  # Se o arquivo não existir, começa com lista vazia

    def salvar_no_arquivo(self):
        with open(self.arquivo, 'w') as f:
            for usuario in self.usuarios:
                f.write(f"{usuario['nome']},{usuario['email']}\n")

    def cadastrar(self, usuario):
        self.usuarios.append(usuario)
        self.salvar_no_arquivo()

    def listar_todos(self):
        return self.usuarios

    def buscar_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.get('email') == email:
                return usuario
        return None

    def remover(self, email):
        self.usuarios = [usuario for usuario in self.usuarios if usuario.get('email') != email]
        self.salvar_no_arquivo()

    def atualizar(self, usuario):
        for i, u in enumerate(self.usuarios):
            if u.get('email') == usuario.get('email'):
                self.usuarios[i] = usuario
                self.salvar_no_arquivo()
                break

    def listar_por_nome(self, nome):
        return [u for u in self.usuarios if u.get('nome') == nome]

    def listar_por_email(self, email):
        return [u for u in self.usuarios if u.get('email') == email]

    def listar_por_nome_e_email(self, nome, email):
        return [u for u in self.usuarios if u.get('nome') == nome and u.get('email') == email]


def exibir_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário encontrado.")
    else:
        for u in usuarios:
            print(f"Nome: {u['nome']}, Email: {u['email']}")


def menu():
    repo = UsuarioRepository()
    while True:
        print("\n--- Menu de Usuários ---")
        print("1 - Cadastrar usuário")
        print("2 - Listar todos")
        print("3 - Buscar por email")
        print("4 - Remover usuário")
        print("5 - Atualizar usuário")
        print("6 - Listar por nome")
        print("7 - Listar por email")
        print("8 - Listar por nome e email")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            repo.cadastrar({'nome': nome, 'email': email})
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de Usuários ---")
            exibir_usuarios(repo.listar_todos())

        elif opcao == "3":
            email = input("Email: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                print(f"Encontrado: Nome: {usuario['nome']}, Email: {usuario['email']}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            email = input("Email: ")
            repo.remover(email)
            print("Usuário removido (se existia).")

        elif opcao == "5":
            email = input("Email do usuário a atualizar: ")
            nome = input("Novo nome: ")
            repo.atualizar({'nome': nome, 'email': email})
            print("Usuário atualizado.")

        elif opcao == "6":
            nome = input("Nome: ")
            print("\n--- Usuários com o nome informado ---")
            exibir_usuarios(repo.listar_por_nome(nome))

        elif opcao == "7":
            email = input("Email: ")
            print("\n--- Usuários com o email informado ---")
            exibir_usuarios(repo.listar_por_email(email))

        elif opcao == "8":
            nome = input("Nome: ")
            email = input("Email: ")
            print("\n--- Usuários com nome e email informados ---")
            exibir_usuarios(repo.listar_por_nome_e_email(nome, email))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

