"""
2-Faça um programa que leia um número inteiro fornecido pelo usuário. 
Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. Se o número for negativo,
mostre uma mensagem dizendo que o número é inválido.
"""
from math import sqrt

num = int = int(input("Informe um número inteiro: "))
if num >= 0:
    print(f"A raiz quadrada de {num} é {sqrt (num)}")
else:
    print("O número informado é negativo")


