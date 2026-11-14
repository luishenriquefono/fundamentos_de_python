# Receba nome, peso e altura. Calcule IMC.

# Entrada 
nome = (input(" Digite o seu nome: "))
peso = float(input(" Digite o seu peso: "))
altura = float(input( " Digite a sua altura: "))

# Processamento
# IMC = peso (Kg) / [alura (m) x altura (m)]
imc = peso / (altura * altura)


# Saída
print (f" Seu IMC é: {imc: .2f}")


