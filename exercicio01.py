# 1. Receba a idade em anos e imprima em meses, dias, horas e minutos.


# números, textos e booleanos
# Entrada
idade = int(input("Digite a idade: ")) #pega o texto e converte para número

# processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras= idade * 365 * 24
idadeEmMinutos = idade * 365 * 24 * 60

# saída
print(f" Sua idade em meses é: {idadeEmMeses} meses")
print(f" Sua idade em Dias é: {idadeEmDias} dias")
print(f" Sua idade em horas é: {idadeEmHoras} horas")
print(f" Sua idade em minutos é: {idadeEmMinutos} minutos")