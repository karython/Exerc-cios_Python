primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

condicao1 = primeiro_valor > segundo_valor
condicao2 = primeiro_valor < segundo_valor
condicao3 = primeiro_valor == segundo_valor

if condicao1 == True:
    print(primeiro_valor, 'é maior que o',segundo_valor)
elif condicao2 == True:
    print(segundo_valor, 'é maior que', primeiro_valor)
else:
    print('os valores sao iguais')
    

#codigo simples corrigido
primeiro_valor  =  input( 'Digite um valor: ' )
segundo_valor  =  input( 'Digite outro valor: ' )

if primeiro_valor  >= segundo_valor:
    print (
        f' { primeiro_valor = } é maior ou igual '
        f'ao que { segundo_valor = } '
    )
else :
    print (
        f' { segundo_valor = } é maior '
        f'do que { primeiro_valor = } '
    )