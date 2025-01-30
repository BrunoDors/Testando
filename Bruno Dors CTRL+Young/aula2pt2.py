#F-strings

nome = 'bruno'
print ('nome', nome)

altura = 1.73
print ('altura', altura)

peso = 60
print ('peso', peso)

imc = peso / (1.73 * 1.73)
print ('imc', imc)

print (f'nome {nome}, possui {altura}m de altura, pesa {peso}kg e seu imc é {imc:.2f}')

print ('nome {} altura {} peso {} imc {:.2f}'.format(nome,altura,peso,imc))

