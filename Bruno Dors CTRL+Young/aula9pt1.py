def bem_vindos(nome):
    print('Boas vindas' ,nome, 'a ctrl play')

bem_vindos('Bruno')

def filme_favorito(titulo):
    print(f'um dos meu filmes favorito é {titulo}')

filme_favorito('Star Wars')
filme_favorito('Arcane')
filme_favorito('john Wick')

def velocidade(tempo,distancia):
    print(distancia/tempo)

velocidade(distancia=2 , tempo=4)

def menor(a,b):
    if a < b:
        return(a)
    else:
        return(b)

a = 5
b = 2
print(f'o menor valor entre {a} e {b} é {menor(a,b)}')



