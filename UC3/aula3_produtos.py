from collections import defaultdict

def remover_duplicatas_por_nome(itens):
    """
    Remove duplicatas com base apenas no nome do produto, preservando a ordem
    """
    nomes_vistos = set()
    unicos = []
    for nome, preco, categoria in itens:
        if nome.lower() not in nomes_vistos:
            unicos.append((nome, preco, categoria))
            nomes_vistos.add(nome.lower())
    return unicos

def obter_itens_acima_de_preco(itens, preco_limite):
    return [item for item in itens if item[1] > preco_limite]

def exibir_itens_por_categoria(itens_filtrados):
    categorias = defaultdict(list)
    for item in itens_filtrados:
        categorias[item[2]].append(item)

    print("\nItens encontrados com preço superior ao limite:")
    for categoria, itens_categoria in categorias.items():
        print(f"\nCategoria: {categoria} (Total: {len(itens_categoria)} produtos)")
        for item in itens_categoria:
            print(f"{item[0]} - R${item[1]:.2f}")

def obter_preco_limite():
    while True:
        try:
            preco_limite = float(input("Digite o preço limite para filtrar os itens (ex: 1000): R$ "))
            if preco_limite < 0:
                print("O preço limite não pode ser negativo. Tente novamente.")
            else:
                return preco_limite
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    itens = [
        ("Celular", 1800, "Eletrônicos"),
        ("Cadeira", 450, "Móveis"),
        ("Notebook", 3500, "Eletrônicos"),
        ("Lâmpada", 25, "Casa"),
        ("Monitor", 1300, "Eletrônicos"),
        ("Cafeteira", 220, "Casa"),
        ("Smartwatch", 850, "Eletrônicos"),
        ("Sofá", 2500, "Móveis"),
        ("Mesa", 900, "Móveis"),
        ("Geladeira", 2800, "Casa"),
        ("Fogão", 2500, "Casa"),
        ("Cômoda", 1200, "Móveis"),
        ("Estante", 1500, "Móveis"),
        ("Ar Condicionado", 3200, "Casa"),
        ("Máquina de Lavar", 1800, "Casa"),
        ("Cama Box", 1800, "Móveis"),
        ("Micro-ondas", 1200, "Casa"),
        ("Poltrona", 700, "Móveis"),
        # Duplicatas
        ("Celular", 2000, "Promoção"),
        ("Geladeira", 2900, "Eletrodomésticos"),
        ("Sofá", 2700, "Sala"),
        ("Cama Box", 1600, "Quarto"),
        ("Fogão", 2400, "Promoção"),
        ("Estante", 1700, "Quarto"),
        ("Poltrona", 800, "Sala")
    ]

    preco_limite = obter_preco_limite()
    itens_filtrados = obter_itens_acima_de_preco(itens, preco_limite)
    exibir_itens_por_categoria(itens_filtrados)

    comando = input("\nDeseja remover duplicatas? Digite: remove duplicatas\n> ").strip().lower()
    if comando == "remove duplicatas":
        print("\nRemovendo duplicatas por nome...")
        itens_sem_duplicatas = remover_duplicatas_por_nome(itens_filtrados)
        exibir_itens_por_categoria(itens_sem_duplicatas)
    else:
        print("\nNenhuma duplicata foi removida.")

main()





