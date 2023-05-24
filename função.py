# > FUNÇÕES

# 1.Funções já aprendidas
"""print()
input()
len()
max()"""

# 2. Criação de funções

#Função inicial

def saudação ():
    print("Seja bem-vindo")

saudação() #isso permite o código rodar

#Função com parâmentros

def saudação(nome, curso):
    print(f"Seja bem-vinda, {nome}")
    print(f"Olá, é um prazer ter você participando do curso de {curso}")

saudação("Samara", "python")



#Função com parâmetros default

def saudação(nome, curso="python"): #nesse caso, não preciso colocar o valor 'pyhon' na saudação.
    print(f"Seja bem-vinda, {nome}")
    print(f"Olá, é um prazer ter você participando do curso de {curso}")

saudação("Samara") 

#Funçoes com retorno

def soma(num1, num2):
   return num1 + num2 #só pode ser usado no final do código, pois tudo que imprimo depois não vai funcionar


   """ print("soma = " num1 + num2)""" #maneira não útil para o objetivo


resultado = soma (5, 7)
print ("O resultado da soma é", resultado)

def calculadora(num1, num2, operação="+"):
    if operação == "+":
        return num1 + num2
    elif operação == "-":
        return num1 - num2
    
resultado = calculadora(10, 20) #só seria subtração caso (10, 20, "-")
print(resultado)