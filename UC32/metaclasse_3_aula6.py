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
