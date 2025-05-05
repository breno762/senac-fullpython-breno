import random

def escolher_palavra():
    palavras = [
        ("python", "É uma linguagem de programação muito popular."),
        ("programacao", "É o processo de escrever código para computadores."),
        ("computador", "Uma máquina que executa tarefas através de programas."),
        ("algoritmo", "É uma sequência de passos para resolver um problema."),
        ("desenvolvimento", "O processo de criar software ou aplicativos."),
        ("inteligencia", "Refere-se à capacidade de aprender e resolver problemas."),
        ("sistema", "Conjunto de componentes que trabalham juntos para realizar uma tarefa.")
    ]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return ' '.join([letra if letra in letras_corretas else '_' for letra in palavra])

def jogo_da_forca():
    while True:
        palavra_secreta, dica = escolher_palavra()
        letras_corretas = set()
        letras_erradas = set()
        tentativas = 6

        print("\nBem-vindo ao Jogo da Forca!\n")
        print("Adivinhe a palavra, você tem 6 tentativas!")
        print(f"Dica: {dica}\n")

        while tentativas > 0:
            print("\nPalavra:", exibir_palavra(palavra_secreta, letras_corretas))
            print(f"Letras erradas: {' '.join(sorted(letras_erradas))}")
            print(f"Tentativas restantes: {tentativas}")

            letra = input("Digite uma letra: ").lower().strip()

            if not letra.isalpha() or len(letra) != 1:
                print("Por favor, digite apenas uma letra.")
                continue

            if letra in letras_corretas or letra in letras_erradas:
                print("Você já tentou essa letra.")
                continue

            if letra in palavra_secreta:
                letras_corretas.add(letra)
                print("Letra correta!")
            else:
                letras_erradas.add(letra)
                tentativas -= 1
                print("Letra incorreta!")

            if all(letra in letras_corretas for letra in palavra_secreta):
                print("\nParabéns! Você venceu!")
                print("A palavra era:", palavra_secreta)
                break

        if tentativas == 0:
            print("\nGame over! A palavra era:", palavra_secreta)

        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

jogo_da_forca()
