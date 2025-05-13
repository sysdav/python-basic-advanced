"""
Condicionais em python

if - se
elif - se
else
"""
idade = 10

#if idade > 18:

    #print("Maior de idade") #true
#elif idade == 18:
    #print("Maior de idade")
#else:
    #print("menor de idade") # false




# 1. Verificar se um número é positivo, negativo ou zero

num = -0.3


if num == 0:
    print("zero")
elif num < 0:
    print("Numero negativo")
else:
    print("numero positivo")

# 2. Verificar se uma pessoa é maior de idade

idade = 2

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

#4 . Classificar a nota de um aluno
# fui alem fiz uma aritimetica

nota1 = int(input("digite a primeira nota"))
nota2 = int(input("digite a segunda nota"))
nota3 = int(input("digite a terceira nota"))

media = nota1 + nota2 + nota3 /3

if media >= 5:
    print("Aprovado")
elif media >= 3:
    print("Recuperacao")
else:
    print("Reprovado")

    # maior ou igual a 5 aprovado
    # maior ou igual a 3 recuperacao
    # menor que 3 reprovado