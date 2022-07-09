# Variáveis

# números

velocidade_internet = 10
print(velocidade_internet)

# float (números decimais)

# nota_filme = 8.5

# valores boleanos

# esta_aberto = True

# strings (texto)

# nome_curso = "Lógica de Programação"

#como variáveis seriam usadas em um programa real?
#problema 1 - Valor Hora
#escreva um programa q retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhas por mês.
# ''''''
# --pseudocódigo--
# input salario_mensal
# input horas_trabalhas_por_mes
# valor_hora = salario_mensal / horas_trabalhadas_por_mes
# print valor_hora
# ''''''

salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)


