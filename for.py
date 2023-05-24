# > REPETIÇÃO

"""
for variavel in range(10):  #imprime os números de 0 a 9
    print (variavel)


for variavel in range(1, 10):  #imprime os números de 1 a 9
    print (variavel)


for variavel in range(1, 12, 3):  #último número é o salto
    print (variavel)

"""

soma= 0 #isso é pra fazer a soma das notas


for i in range (1, 4):
    nota = float(input(f"Informe a sua nota {i}: ")) 
     #o f e as chaves {} são pra informar nota 1, 2 etc
    soma = soma + nota

print (soma/3)
