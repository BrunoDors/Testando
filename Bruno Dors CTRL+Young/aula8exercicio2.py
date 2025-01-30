#crie uma tupla e escreva um programa que verifique se um detrminado elemento esta presente nela

tupla1 = (1,2,3,4,5)
A = (int(input('Digite um numero de 1 ao 5: ')))
if A in tupla1:
    print('esta na tupla')
else:
    print('não esta na tupla')

