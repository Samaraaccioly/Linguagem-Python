# > REPETIÇÃO

numero_sortedo = 15

numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

while numero_sortedo != numero_escolhido:
    print ("Você errou")
    print ("Tente novamente...")

    numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

print ("Parabéns, você acertou!!! ")

#Exemplo 2: estrutura com contador

contador = 0

while contador < 5:
    print (contador)

    contador = contador + 1