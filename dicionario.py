# > DICIONÁRIOS

#Criando dicionários

dicionario = {}
dicionario = dict()

dicionario ={"nome": "Samara", "idade" : "21", "altura": "1.6"}

print(dicionario)
print(dicionario["idade"]) #encontrar um elemento do dicionário


#Adicionando elementos em um dicionário

dicionario ["programador"] = True
print(dicionario)

dicionario ["altura"] = 2
print(dicionario) #substitui a altura original

#Iterando sobre um dicionário

for variavel in dicionario:
    print(variavel) #percorre as chaves

for chave in dicionario:
    print(chave, dicionario[chave])


#Testando a existência de uma chave

print("peso" in dicionario)
print("altura" in dicionario)