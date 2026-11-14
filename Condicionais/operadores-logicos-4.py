# operadores lógicos
# and - ambas as expressões devem retornar verdadeiras
# or - apenas uma das expressões devem retornar verdadeira
# not - inverte o resultado da expressão lógica


idade = int(input("Qual é sua idade? "))
ingresso = input("Vocetem ingresso? s/n ")


# conjugar com operador and
if idade  >= 18 or ingresso == "s" :
    print (" Seja bem-bem vindo à festa 🥳🎉")

else :
    print(" Você não pode entrar na festa")