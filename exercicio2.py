nome = 'karython'
altura = 1.75
peso = 84
imc = peso / (altura * altura) #peso / altura ** 2

#f-strings para formatar linhas
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu ICM é imc'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)


