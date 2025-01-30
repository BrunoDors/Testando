convidados = ['jose', 'lucas', 'ana', 'enzo', 'valentina']
print('primeiro convidado da festa: ' + convidados[0])

convidados[0] = 'joao'
print(convidados)

convidados.append('larissa')                   # .append serve para colocar um nome no final da lista
print(convidados)

convidados.insert(0, 'joao')                   # .insert serve para posicionar o 'nome'
print(convidados)

#del convidados[3]                              # del serve para remover algum 'nome' 
#print(convidados)

convidadoremovido = convidados.pop(0)          #serve para deletar algum 'nome' porem ele serve tambem para
print(convidadoremovido)                       #remover de tras pra frente, ultimo = -1

viajando = 'ana'
convidados.remove(viajando)                    #remove o nome pelo nome
print(convidados)
print(viajando + ' não ira a festa pois esta viajando')

convidados.sort()                            #sort() altera a posição de itens em uma lista para colocá-los em ordem alfabética
print(convidados)

convidados.sort(reverse=True)                #sort() altera a posição de itens em uma lista para colocá-los em ordem alfabética
print(convidados)                            #para deixar de tras pra frente,colocar 'reverse=true'

print(sorted(convidados))                    # sorted serve para mostrar em ordem alfabetica porem nao altera a lista
print(convidados)

convidados.reverse()                         
print(convidados)

print(len(convidados))                      # len mostra quantidade

numeros = list(range(1,5))                  #mostra a distancia mas nunca mostra o ultimo valor
print(numeros)

print(min(numeros))                         #mostra o minimo ou o primeiro numero

print(max(numeros))                         #mostra o maximo ou ultimo numero

print(convidados[2:4])                      # : serve para fatiar

convidados2 = convidados[:]
print(convidados2)















