#  Elabore um programa para cálculo de preços de produtos que solicite o preço de compra do produto e o percentual a ser aplicado em cima desse valor para a venda. Calcule e exiba o preço de venda do produto. Se o percentual a ser aplicado for inferior a 50%, exiba uma mensagem informando ao usuário que o produto será vendido com uma margem muito pequena de lucro.
print() #pular linha
print() #pualar linha

print("|********************************************************************************************************|")
print("|Programa para calcular o preço de venda de um produto com base no preço de compra e percentual de lucro |")
print("|                                        Versão 1.0 - 2026                                               |")
print("|********************************************************************************************************|")


print() #pular linha

# Entrada
precoCompra = float(input(" Digite o valo do do produto: "))
porcentualLucro = float(input(" Digite o porcentual de lucro que deseja aplicar: "))

# outra opção de entrada
# percentualAplicado = float(input("Digite o porcentual a ser aplicado : ")

print() #pular linha

#Processamento
if porcentualLucro <= 50: #True
    precoVenda = precoCompra * (1 + (porcentualLucro / 100))
    print("O produto será vendido com uma margem muito pequena de lucro")

else: #False
    precoVenda = precoCompra * (1 + (porcentualLucro / 100))
    print("O produto será vendido com uma margem de lucro satisfatória")

# outra opção de processamento
# precoVenda = precoCompra + (precoCompra * percentualAplicado / 100)
# Caso queira colocar a porcentagem:
# if percentualAplicado < 50 :
# print("Percentual inferior a 50% - o produto será vendido com margem pequena de lucro")


print() #pular linha
# Saída
print(f'O preço de venda do produto é: R$ {precoVenda: .2f}')

print() #pular linha
print("Fim do programa")
