# Uma empresa decide dar aumento de 30% aos funcionários cujo salário é inferior a 500 reais. Escreva um programa que receba o salário de um funcionário e imprima ovalor do salário reajustado ou uma mensagem caso o funcionário não tenha direito a aumento.

print(" Algoritmo para calcular o sakário de um funcionário com aumento de 30% caso o salário seja menor que 500 reais")

print() #pular linha

# Entrada
salario = float(input("Digite o seu salário: "))

print() #pular linha

# Processamento
if salario < 500 : # true
    salarioAumento = salario * 1.30
    print (f' O salário do funcionário com aumento de 30% é: R$ {salarioAumento: .2f}')

else : # false
    print (f' o salário do funcionário é: R$ {salario: .2f} e não tem direito a reajuste de 30%')

print() #pular linha
print("Fim do programa")