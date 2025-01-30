#escreva um programa que leia a velocidade de um carro 
#Se ele ultrapassar 80km por hora, mostre a mensagem dizendo que ele foi multado
#mostre tambem o valor da multa de R$7,00 pra cada km acima da valocidade 

velocidade = int(input('velocidade: '))

if velocidade > 80:
   print(f'Voce foi multado em {(velocidade - 80)*7 }')



