#Desenvolva um programa que pergunta a distancia de um viagem em km 
#calcule o preço do passagem, cobrando 0,50 para viagem ate 200km
#e 0,45 para viagens mais longas 

viagem = float(input('Digite quantos km tem sua viagem: '))

if viagem <= 200.00:
   print(f'Sua viagem custara {viagem * 0.50}')

if viagem > 200.0:
   print(f'Sua viagem custara {viagem * 0.45}')