numero_de_funcionarios = int(input('Digite um numero de funcionarios: '))
horas_trabalhadas = int(input('Digite um numero de horas trabalhadas: '))
valor_hora = float(input('digite o quanto voce recebe por hora: '))

print(horas_trabalhadas * valor_hora)
print(f'O numero do funcionario {numero_de_funcionarios} trabalhou {horas_trabalhadas} horas e recebeu R${valor_hora} ')
