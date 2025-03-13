nome = "João"
idade = 25
print (nome, idade)

a = 10
b = 5
print("Soma:", a + b)
print("Subtração", a - b)
print("Multplicação:", a * b)
print("Divisão:", a / b)

primeiro_nome = "Maria"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo) 

x = 15
y = 20
print("x é maior que y?", x > y)
print("x é igual a y?", x == y)

tem_carteira = True
idade = 18
tem_carro = False
pode_dirigir = idade >= 18 and tem_carteira
print("pode dirigir?", pode_dirigir)
print("pode dirigir e tem carro?", pode_dirigir)

frase = "python é divertido"
print(frase.upper())
nova_frase = frase.replace("divertido", "poderoso")
print(nova_frase)

contador = 0
contador += 5
contador -= 2
contador *= 3
print("valor final do contador:", contador)

a = 10
b = 20
c = 30
media = (a + b + c) / 3
print("média", media)
print("A média é maior que 15 e menor que 25?", 15 < media < 25)

nota = 75
if nota >= 60:
    print("Aprovado")
elif nota >= 40:
    print("Recuperação")
else:
    print("Reprovado")


