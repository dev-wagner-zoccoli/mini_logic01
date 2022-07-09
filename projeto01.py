# Fatorial de um número
# Crie um programa q recebe um número e imprime seu fatorial.
#  - Método 5 Q -
# 1. informar número a ser calculado o fatorial
# 2. calculo do fatorial do número informado
# 3. o número informado deve ser inteiro e positivo
# 4. exibir na tela o resultado do fatorial do número informado
# 5. 
#   - input número
#   - número > 0
#   - número = inteiro
#   - fatorial = 1
#   - loop 1 a número
#       fatorial = fatorial * numero
#   - print fatorial

answer = int(input('Informe o número do qual vc quer extrair o fatorial: '))
if answer > 0:
    f = 1
    for iten in range(1,answer + 1):
        f = f * iten
    print(f)

