# Faça um programa que receba 15 números inteiros e imprima na tela a somatória dos 15 números.

print() #pular linha
print() #pular linha

print("|********************************************************************************************************|")
print("|          Programa para receber 15 números inteiros e mostrar a somatória dos números ao final           |")
print("|                                        Versão 1.0 - 2026                                               |")
print("|********************************************************************************************************|")

print() #pular linha
print() #pular linha

# Entrada
total = 0

# Processamento
for x in range (1, 16) :
    n = int(input(" Digite um número"))
    total - total + n

# Saída
    print(f"A Soma de todos os números é: {total}")