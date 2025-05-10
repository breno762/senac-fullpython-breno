class UsuarioRepository:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        """Cadastra um novo usuário (dicionário com 'nome' e 'email')."""
        self.usuarios.append(usuario)

    def listar_todos(self):
        """Retorna a lista de todos os usuários."""
        return self.usuarios

    def buscar_por_email(self, email):
        """Retorna o primeiro usuário com o email informado, ou None se não encontrar."""
        for usuario in self.usuarios:
            if usuario.get('email') == email:
                return usuario
        return None

    def remover(self, email):
        """Remove o usuário com o email informado."""
        self.usuarios = [usuario for usuario in self.usuarios if usuario.get('email') != email]

    def atualizar(self, usuario):
        """Atualiza os dados do usuário com o email correspondente."""
        for i, u in enumerate(self.usuarios):
            if u.get('email') == usuario.get('email'):
                self.usuarios[i] = usuario
                break

    def listar_por_nome(self, nome):
        """Retorna todos os usuários com o nome informado."""
        return [u for u in self.usuarios if u.get('nome') == nome]

    def listar_por_email(self, email):
        """Retorna todos os usuários com o email informado."""
        return [u for u in self.usuarios if u.get('email') == email]

    def listar_por_nome_e_email(self, nome, email):
        """Retorna todos os usuários com o nome e email informados."""
        return [u for u in self.usuarios if u.get('nome') == nome and u.get('email') == email]


if __name__ == "__main__":
    repo = UsuarioRepository()

    repo.cadastrar({'nome': 'Alice', 'email': 'alice@example.com'})
    repo.cadastrar({'nome': 'Bob', 'email': 'bob@example.com'})
    repo.cadastrar({'nome': 'Alice', 'email': 'alice2@example.com'})

    print("Todos os usuários:")
    print(repo.listar_todos())

    print("\nBuscar por email 'alice@example.com':")
    print(repo.buscar_por_email('alice@example.com'))

    print("\nRemover usuário com email 'bob@example.com'")
    repo.remover('bob@example.com')
    print(repo.listar_todos())

    print("\nAtualizar usuário com email 'alice@example.com'")
    repo.atualizar({'nome': 'Alice Atualizada', 'email': 'alice@example.com'})
    print(repo.listar_todos())

    print("\nListar por nome 'Alice':")
    print(repo.listar_por_nome('Alice'))

    print("\nListar por email 'alice2@example.com':")
    print(repo.listar_por_email('alice2@example.com'))

    print("\nListar por nome e email 'Alice Atualizada' e 'alice@example.com':")
    print(repo.listar_por_nome_e_email('Alice Atualizada', 'alice@example.com'))
