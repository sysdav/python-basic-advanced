# Comentario simples
"""
Comentario em bloco.
"""
# PEP8 - Python enhancement proposal 8
# Python proposta de melhoria 8

# algumas melhorias que podem ajudar no codigo.

#-[1] Utilizar Camel Case para classes
class Calculadora:
    pass

class Cientifica:
    pass

#-[2] Ao criar nomes de variaveis e funcoes sempre minusculo e separalas por udnerline.

nome = "david"
sobrenome = "william"
nome_completo = nome + " " + sobrenome
print(nome_completo)

def soma():
    pass

def multiplicacao():
    pass

#-[3] Indentar o codigo com spaces.
#-[4] Sempre dentro de uma class dar espaco de uma linha para cada funcao.
#-[5] Imports

#- Import errado.

#import sys,os

#- Import certo.

#import os
#import sys
#import this

# caso tenha muitos imports

# from types import (
#   StringType,
#   ListType,
#   SetType,
#   AnotherType
#   )
