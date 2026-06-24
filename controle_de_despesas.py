'''Perguntar quantas despesas deseja cadastrar.
Solicitar o nome da despesa.
Solicitar o valor.
Somar tudo.
Mostrar:
Quantidade de despesas
Valor total
Maior despesa'''
qtd_despesas = int(input('Quantas despesas deseja cadastrar? '))
despesas = []
for d in range(1,qtd_despesas+1):
    nome_despesa = input('Qual o nome da despesa? ')
    valor_despesa = float(input(f'Qual o valor {nome_despesa}: '))
    despesa = (nome_despesa,valor_despesa)
    despesas.append(despesa)
for despesa in despesas:
    print(despesa)   
  