#Entrada de dados
#Exemplo de código versões 2 do python
'''
print("Qual o seu nome ?")
nome = input ()
print('Seja bem-vindo(a) %s'%nome)
print("Qual a sua idade ?")
idade = input()
print('%s tem %s anos'%(nome,idade))
'''
#Exemplo de código versões 3 python
'''
print("Qual o seu nome ?")
nome = input()
print('Seja bem-vindo(a) {0}'.format(nome))
print('Qual a sua idade ?')
idade = input()
print('{0} tem {1} anos'.format (nome,idade))
'''
#Exemplo de código versão 3.7 python
'''
print("Qual o seu nome ?")
nome = input()
print(f'Seja bem-vindo(a) {nome}')
print("Qual a sua idade ?")
idade = input()
print(f'A {nome} tem {idade} anos')
'''
#Exemplo de código versão atual
nome = input('Qual o seu nome ?')
print(f'Seja bem-vindo(a) {nome}')
idade = int(input('Qual a sua idade ?'))
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {2018 - idade}')