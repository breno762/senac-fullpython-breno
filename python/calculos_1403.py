numero = int(input("Digite um número para iniciar a contagem regressiva: "))
for i in range(numero, -1, -1):
    print(i)

numero = int(input("Digite um número para somar todos os números de 1 até ele: "))
soma = 0
contador = 1
while contador <= numero:
    soma += contador
    contador += 1
    print(f"A soma de todos os números de 1 até {numero} é: {soma}")

numero = int(input("Digite um número para ver a tabuada dele de 1 a 10: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

numero = int(input("Digite um número para ver todos os números pares de 1 até ele: "))
print(f"Números pares de 1 até {numero}:")
for i in range(1, numero + 1):
    if i % 2 == 0:  # Verifica se o número é par
        print(i)