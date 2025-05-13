#1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.

print("digite dois numeros inteiros:")
valor1 = int(input("primeiro numero: "))
valor2 = int(input("segundo numero: "))

if valor1 > valor2:
    print(f'valor {valor1} e maior e {valor2} e menor')
else:
    print(f'valor {valor2} e maior {valor1} e menor')