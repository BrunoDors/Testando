#escreva um programa que leia dois numeros inteiros e compare os mostrando na tela a mensagem:
#O primeiro valor é maior: 
#Ou o segundo valor é maior: 
#Ou se ambos os valores sao iguais: 

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

if numero1 >= numero2: 
    print(f'O {numero1} é maior que o {numero2}')

elif numero1 <= numero2:
    print(f'O {numero1} é menor que o {numero2}')

elif numero1 == numero2:
    print(f'Seu numero é igual')

else: 
    print(f'Seu numero não é igual a nada')