with open('Intervalo.txt', 'w') as arquivo:
    valor = int(input('Digite um numero de 0 a 100: '))
    
with open('intervalo.txt', 'r') as arquivo:
    if 0 <= valor <= 25: 
        print('esta dentro do intervalo 0 e 25')
    elif 25 < valor <= 50:
        print('esta dentro do intervalo 25 e 50')
    elif 50 < valor <= 75:
        print('esta dentro do intervalo 50 e 75 ')
    elif 75 < valor <= 100: 
        print('esta dentro do intervalo 75 e 100')
    else: 
        print('valor fora do intervalo')

 

    