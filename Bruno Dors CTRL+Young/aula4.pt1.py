string1 = 'oi'

string2 = 'bem vindo a ctrlplay'

string3 = "podemos tambem usar aspas duplas"

print(string1)
print(string2)
print(string3)

print('sejam bem vindo\na\naula 4')                                #serve para colocar o texto a baixo \n

print('ola \t ctrl play')                                         #deixa um espaçamento entre uma palavra entre outra \t

frase = 'nos somos uma escola de programação e robotica'
print(len(frase))                                                   #conta o numero de caracteres (inclusive o espaço)

print(frase[10])                                                   #serve para dizer qual letra é diante de um numero (começa do 0)

print(frase[7:])                                                    #serve para cortar um pedaço do texto (numero determina isso)

print(frase[:7])                                                  #serve para cortar uma frase de frente pra tras (numer determina isso)

print(frase[10:15])                                               #ele vai pegar so uma pedaço do texto (ex: o 10 aparece o 15 
                                                                   #não aparece, como se fosse do 10 ao 14

print(frase[-1])                                                  #sere para mostrar a letra de frente p traz (o sinal indica isso)

print(frase[::2])                                                #serve para pular letras

print(frase[1:10:2])                                              #pula de letra em letra e ate um fim determinado
                                                                 # 1 = numero inicial / 10 = numero limite / 2 = pula letra

print(frase[2::3])                                               #serve para pular letra 2 = inicio 3 = letras pulada

email = 'fulano@ctrlplay.com.br'
print(email.find('.'))                                          #serve para encontrar uma letra (começa pelo 0)
                                                                #caso n tenha o caracter ele da -1

print(email.count('.'))                                         #da o numero de quantos caracteres tem na frase

nome = 'José'
sobrenome = ' Bond'
print(nome + sobrenome)

print(sobrenome*5)


numeroIrmaos = 2
                                                            
                                                         #só pode str com str, caso coloque um int tem q fzr a conversão botado str
print('voce tem ' + str(numeroIrmaos) + 'irmaos')

exemplo = 'ctrl+play - escola de programação e robotica'
print(exemplo.upper())                                      #UPPER vai deixar tudo maiusculo

print(exemplo.lower())                                      #LOWER fica tudo minusculo 

cadaPalavra = exemplo.split()                              #separa por espaços
print(cadaPalavra)

print(cadaPalavra[2])                                       #determina a palavra (começando do 0)

cadaPalavra = exemplo.split('-')
print(cadaPalavra[1])

nome = input('Digite seu nome: ')
print(f'Olá {nome}')











