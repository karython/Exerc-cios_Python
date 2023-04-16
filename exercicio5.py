"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
numero = float(input("Digite um numero inteiro: "))

resto = numero % 2 #verifica se o resto da divisão é 0 ou nao


if resto == 0:
        print(f'O número {numero} é par')
else:
        print(f'O numero {numero} é impar')





Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação coletiva. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.


saudacao = float(input('Digite a hora: '))

try: #para transformar a string em inteiro (usar try e except)
    if saudacao >=0 and saudacao <=11:
        print("Bom Dia!")
    elif saudacao >=12 and saudacao <=17:
        print('Boa Tarde!')
    elif saudacao >=18 and saudacao <=23:
        print('Boa Noite!')
    else:
         print("Não conheço essa hora")
except:
    print("Digite um valor inteiro")



Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
primeiro_nome = input("Digite seu nome: ")
letras = len(primeiro_nome)

if letras >1:
    if letras <=4:
        print(f'Seu nome é curto')
    elif letras >=5 and letras <=6:
        print(f'Seu nome é normal')
    elif letras >6:
        print(f'Seu nome é longo')
else:
    print(f'Digite mais de uma letra')