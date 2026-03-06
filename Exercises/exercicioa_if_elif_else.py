"""
1- Faça um programa que receba dois números inteiros e mostre qual deles é o maior:
"""
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

if n1 > n2:
    print(f"O maior número é o {n1}")
elif n1 == n2:
    print(f"Os dois números são iguais")
else:
    print(f"O número maior é {n2}")
"""
2-Faça um programa que leia um número inteiro fornecido pelo usuário. 
Se esse número for positivo, calcule a raiz quadrada do número e apresente-a. Se o número for negativo,
mostre uma mensagem dizendo que o número é inválido.
"""
num = int(input("Informe um número inteiro: "))
if num >= 0:
    quad = num ** 0.5
    print(f"A raiz quadrada de {num} é {quad}")
else:
    print("O número informado é negativo")

"""
3-Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
"""
nb = int(input("Digite um número inteiro: "))
if nb % 2 == 0:
    print(f"O número {nb} é par")
else:
    print(f"O número {nb} é ímpar")
