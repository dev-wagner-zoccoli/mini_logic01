# Programa q gera valor aleatório de 1 a 10, usuário chuta número até acertar. Programa deve informar se chute foi acima, abaixo ou acerto.

# 1. random n; guess
# 2. compare input data
# 3. n != 0; 1 a 10
# 4. return: guess less, more or correct! to random n
# 5.
# - random n
# - input guess
# - random n == guess
# - if true
#   print correct!
# - elif false
#   guess > random n
#   print less
#   guess < random n
#   print more
# - go till guess = random n

import random

n = random.randint(1,10)

cGuess = False
while cGuess == False:
    guess = int(input("Valor gerado! Chute um valor de 1 a 10: "))
    if guess > n:
        print("Seu chute é maior q o valor gerado.")
    elif guess < n:
        print("Seu chute é menor q o valor gerado.")
    else:
        print("Correto!")
