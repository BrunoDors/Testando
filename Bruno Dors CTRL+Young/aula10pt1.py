with open('arquivo.txt','w') as arquivo:         #with é pra fechar com segurança algo e 'w' igual a write
    arquivo.write('somos a ctrl play, escola de progrmção e robotica\n')     #\n é pra criar nova linha
    arquivo.write('simpsons\n')


with open('arquivo.txt','a') as arquivo:            #'a' é igual a append(adicionar)
    arquivo.write('novo exemplo adicionado')


with open ('arquivo.txt','r') as arquivo:         #'r' é igual a read(ler)
    conteudo = arquivo.read()
    print(conteudo)







