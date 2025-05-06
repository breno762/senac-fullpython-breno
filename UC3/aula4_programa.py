import os

def listar_usuarios():
    if not os.path.exists("usuarios.txt"):
        print("Nenhum usuário encontrado.")
        return

    with open("usuarios.txt", "r") as file:
        usuarios = file.readlines()

    if usuarios:
        print("Lista de Usuários:")
        for usuario in usuarios:
            nome, email = usuario.strip().split(",")
            print(f"Nome: {nome}, Email: {email}")
    else:
        print("Nenhum usuário encontrado.")

def excluir_usuario(nome):
    if not os.path.exists("user_json"):
        print("Nenhum usuário encontrado.")
        return

    with open("usuarios.txt", "r") as file:
        usuarios = file.readlines()

    with open("usuarios.txt", "w") as file:
        usuario_excluido = False
        for usuario in usuarios:
            if usuario.strip().split(",")[0] != nome:
                file.write(usuario)
            else:
                usuario_excluido = True

        if usuario_excluido:
            print(f"Usuário {nome} excluído com sucesso.")
        else:
            print(f"Usuário {nome} não encontrado.")

def adicionar_usuarios_exemplo():
    usuarios_exemplo = [
        ("João Silva", "joao.silva@email.com"),
        ("Maria Oliveira", "maria.oliveira@email.com"),
        ("Carlos Souza", "carlos.souza@email.com"),
        ("Ana Costa", "ana.costa@email.com"),
        ("Pedro Lima", "pedro.lima@email.com"),
        ("Juliana Almeida", "juliana.almeida@email.com"),
        ("Fernanda Pereira", "fernanda.pereira@email.com"),
        ("Rafael Gomes", "rafael.gomes@email.com"),
        ("Tatiane Rocha", "tatiane.rocha@email.com"),
        ("Ricardo Alves", "ricardo.alves@email.com"),
        ("Luciana Santos", "luciana.santos@email.com"),
        ("Gustavo Martins", "gustavo.martins@email.com"),
        ("Larissa Oliveira", "larissa.oliveira@email.com"),
        ("Felipe Costa", "felipe.costa@email.com"),
        ("Mariana Cruz", "mariana.cruz@email.com")
    ]
    
    for nome, email in usuarios_exemplo:
        (nome, email)
        print(f"Usuário {nome} adicionado.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Excluir Usuário")
        print("4. Adicionar Usuários de Exemplo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o e-mail do usuário: ")
            (nome, email)
            print("Usuário adicionado com sucesso.")
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            nome = input("Digite o nome do usuário a ser excluído: ")
            excluir_usuario(nome)
        elif opcao == "4":
            adicionar_usuarios_exemplo()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

