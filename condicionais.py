"""
Estruturas condicionais
if(se) , else, elif
"""
idade = int(input("Qual a sua idade ?"))
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")
#aqui podemos ter vários elif's mais somente um if e um else