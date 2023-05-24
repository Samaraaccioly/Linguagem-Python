# > ESTRUTURAS CONDICIONAIS

idade = 22

if idade >= 18: #se
    print ("Você é maior de idade")
else: #senão 
    print ("Você é menor de idade")  

    """
    Exemplo: aprovar um aluno, caso a média dele seja maior ou igual a 7, ou reprovar, caso a média das notas seja menor que 7.
    """  

 
media = float ( input ("Informe a média do estdante: "))

if media >= 7:
    print ("O aluno está aprovado")
elif media >= 5:  #else if é encurtado no python p/ elif
    print ("Recuperação")
else: 
    print ("O aluno está reprovado")


#Operação conjunta

nota_media = 10
presença = 100

if nota_media >= 7 and presença >= 70:
    print ("Aluno aprovado")
else:
    print ("Aluno reprovado")