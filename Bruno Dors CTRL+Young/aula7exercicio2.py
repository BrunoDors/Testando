#peça ao usuario um numero para inserir numeros postivos e some os.
#o programa deve continuar pedindo numeros ate que o usuario digite
#um numero negativo, momento em que ele deve exibir o total acumulado

soma = 0 

while True:
    numero = int(input('digite um numero (useo o sinal negativo para parar): '))
    if numero < 0:
        break
    soma = soma + numero

print(f'A soma dos numeros digitados é {soma}')
