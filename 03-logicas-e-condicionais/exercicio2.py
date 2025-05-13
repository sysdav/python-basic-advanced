#Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
#a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
#número é inválido.

from math import sqrt

numero = int(input("forneca um numero inteiro: "))


if numero >= 1:
    print(f"{sqrt(numero)}")
else:
    print("número é inválido")