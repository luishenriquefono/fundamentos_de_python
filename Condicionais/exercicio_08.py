# Faça um programa que receba o nome, cargo e salário de um funcionário. Se o funcionário ganhar abaixo de 1000 reais, calcule o salário acrescido de 10%. Ao final exiba o nome, o cargo e o salário desse funcionário. exiba o nome, o cargo e o salário desse funcionário.

print() #pular linha
print() #pular linha
print("|********************************************************************************************************************|")
print("|  Algoritmo para calcular o salário de um funcionário com aumento de 10% caso o salário seja menor que 1000 reais.  |")
print("|                                               Versão 1.0 - 2026                                                    |")
print("|********************************************************************************************************************|")
print() #pular linha

# Entrada
nome = input(" Digite o seu nome: ")
print() #pular linha
Cargo = input(" Digite o seu cargo: ")
print() #pular linha
salario = float(input(" Digite o seu salário: "))

print() #pular linha

# Processamento
if salario < 1000 : # true
    salarioAumento = salario * 1.10
    print (f'O salário do funcionário {nome} com o cargo de {Cargo} com aumento de 10% é: R$ {salarioAumento: .2f}')

else : # false
    print (f'O salário do funcionário {nome} com o cargo de {Cargo} é: R$ {salario: .2f}')

print() #pular linha
print("Fim do programa")
