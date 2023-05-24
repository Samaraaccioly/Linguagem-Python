# > LISTAS

# Antes
nota1 = 10
nota2 = 9
nota3 = 8

# Com listas
notas = [10, 9, 8] #colchetes[ ]cria listas de varias notas


# Criando lista
lista = [] #lista vazia
lista = list () #lista vazia
lista = [21, "samara", 1.6180, True]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices (fatiamentos)

lista = [256, "Samara", 3.14, False]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) #remete ao ultm elemento, -2 ao penultm...

# Slices

lista = [60, 10, 30, 50, 5]

print(lista[0:3]) #escolhe os três primeiros
print(lista[3:5]) #vai do quarto até o quinto

# Iterações com for

#1. Utilizando os próprios elementos da lista

for elemento in lista:  #conta os elementos
    print(elemento)

#2. Utilizando os indices

print ("Comprimento da lista", len (lista)) #len de length

for i in range (len(lista)):
    print(i)


#> MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

#Append --add elementos no final da lista--

print ("Antes do append ", lista)

lista.append(3) #add um elemento no final da lista

print("Depois do append: ", lista)


#Insert --inserir elementos na posição que quero--

lista.insert(2, 10) #eu escolho qual a posição o elemento vai ocupar na lista. Nesse caso, o número 10 ocupa o 2°

print("Depois do insert: ", lista)


#Extend --juntar elementos--

lista2 = [1, 2, 3]

lista.extend(lista2) #serve para juntar duas listas

print("Depois do extend: ", lista)


#Pop --remover elementos--

lista.pop() #cm parenteses vazio remove o ultm

print("Lista após o pop: ", lista) 

lista.pop(0) #0 é a posição

print("Lista após o pop: ", lista)

#Remove --remove o elemento que eu digito--

lista.remove(3) #Só remove o primeiro 3, caso haja repetido

print("Depois do remove: ", lista)


#Count --conta os elementos--

print("Quantidade de 2 na lista: ", lista.count(2))


#Index --saber a posição do elemento--

print("Qual o indice do elemento 12: ", lista.index(12))


#Sort --ordenar a lista--

lista.sort() #ordem crescente

lista.sort(reverse=True) #ordem decrescente

print(lista)

"""
#FUNÇÕES PARA LISTAS

1. Len
print(len(lista)) --saber o comprimento da lsita--

2. Sum
print(sum(lista)) --soma todos os elementos--

3. Max
print("Maior elemento da lista: ", max(lista)) --saber o maior elemento--

4. Min
print("Menor elemento da lista: ", min(lista)) --saber o menor elemento--
"""

#abaixo repeti as anotações acima

 #len
print(len(lista)) #saber o comprimento da lsita

#sum
print(sum(lista)) #soma todos os elementos

 #max
print("Maior elemento da lista: ", max(lista)) #saber o maior elemento

 #min
print("Menor elemento da lista: ", min(lista)) #saber o menor elemento