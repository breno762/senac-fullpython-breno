class RepositoryMeta(type):
    obrigatorios = {'cadastrar', 'remover', 'atualizar', 'buscar_por_email'}

    def __init__(cls, name, bases, namespace):
        faltando = RepositoryMeta.obrigatorios - set(namespace)
        if faltando:
            raise TypeError(f"A classe '{name}' está faltando os métodos obrigatorios: {faltando}")
        super().__init__(name, bases, namespace)

class UsuarioRepository(metaclass=RepositoryMeta):
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
            pass

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


if __name__ == "__main__":
    repo = UsuarioRepository()

    while True:
        print("\n1. Cadastrar usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por email")
        print("4. Remover usuário")
        print("5. Atualizar usuário")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            usuario = {'nome': nome, 'email': email}
            repo.cadastrar(usuario)
            print(f"Usuário {nome} cadastrado com sucesso.")

        elif escolha == "2":
            usuarios = repo.listar_todos()
            print("Lista de usuários:")
            for usuario in usuarios:
                print(f"Nome: {usuario['nome']}, Email: {usuario['email']}")

        elif escolha == "3":
            email = input("Digite o email para buscar: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                print(f"Usuário encontrado: Nome: {usuario['nome']}, Email: {usuario['email']}")
            else:
                print("Usuário não encontrado.")

        elif escolha == "4":
            email = input("Digite o email do usuário a ser removido: ")
            repo.remover(email)
            print(f"Usuário com email {email} removido.")

        elif escolha == "5":
            email = input("Digite o email do usuário a ser atualizado: ")
            usuario = repo.buscar_por_email(email)
            if usuario:
                nome = input(f"Digite o novo nome para {usuario['nome']} (deixe em branco para manter): ")
                email_novo = input(f"Digite o novo email para {usuario['email']} (deixe em branco para manter): ")
                if nome:
                    usuario['nome'] = nome
                if email_novo:
                    usuario['email'] = email_novo
                repo.atualizar(usuario)
                print(f"Usuário {usuario['nome']} atualizado com sucesso.")
            else:
                print("Usuário não encontrado.")

        elif escolha == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

