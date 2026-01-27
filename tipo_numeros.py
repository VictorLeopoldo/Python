#Números do tipo float:
'''
OBS:
O separador do tipo floar é . e não ,
'''

#Errado do ponto de vista do Float, mas gera uma tupla
"""
valor = 1,44
print(valor)
print(type(valor))
"""
#Certo do ponto de vista do Float
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
"""
valor1, valor2 = 1,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
"""
#Podemos converter um valor float em int
"""OBS: Ao converter valores float para int, perdemos precisão"""
#Exemplo de como uma conversão de float para int pode ter um alto impacto
salario = 2.56
salario1 = 3.67
total = salario + salario1
print(total)
total2 = int(salario) + int(salario1)
print(total2)
print (total - total2)