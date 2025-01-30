def prepara_acai(*ingredientes, tamanho = 'médio'):
    print('\n preparando um açai', tamanho,'com os seguintes ingredientes: ')
    for ingrediente in ingrediente: 
        print('-', ingredientes)

prepara_acai('banana','açai')
prepara_acai('morango','kiwi','leite em pó',tamanho = 'grande')
prepara_acai('banana',tamanho = 'pequeno')
prepara_acai()

