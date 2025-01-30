def menor(lista):
    menorValor = lista[0]
    for x in lista: 
        if (x <menorValor):
            menorValor = x 
    return menorValor 

def maior(lista): 
    maiorValor = lista[0]
    for x in lista: 
        if(x > maiorValor):
            maiorValor = x
    return maiorValor

def maiorEmenor(lista):
    print('maior:', maior(lista))
    print('menor:', menor(lista))

maiorEmenor([4,5,7,2,3,8])

