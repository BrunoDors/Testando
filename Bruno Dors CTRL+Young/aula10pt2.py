with open ('herois.txt','w') as arquivo:
    arquivo.write('homem aranha, marvel\n')
    valor = input('digite algo: ')
with open ('herois.txt', 'a') as arquivo:
    arquivo.write('batman, dc\n')

with open ('herois.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


