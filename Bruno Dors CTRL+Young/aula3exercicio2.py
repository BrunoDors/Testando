montante = int(input('digite um valor em dinheiro: R$'))
meses = int(input('digite um numero de meses: '))
taxa_juros = 0.005            #5%                  #porcentagem 
rendimento = montante * ((1 + taxa_juros) ** meses - 1)

print(f'O rendimento do montante apos {meses} meses sera de R$ {rendimento:.2f}')