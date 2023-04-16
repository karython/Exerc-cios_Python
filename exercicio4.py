nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é:', nome)
    print('Seu nome invertido é:',nome[::-1])
    if ' ' in nome:
        print(f'O nome {nome} contem espaço')
    else:
        print(f'O nome {nome} não contem espaço')
    print(f'Seu nome tem {len(nome)},letras')
    print(f'A primeira letra do seu nome é:',nome[0])
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')