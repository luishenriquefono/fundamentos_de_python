# 2. Receba ano de nascimento e ano atual. Calcule idade e semanas.

# Entrada
anoDeNascimento = int(input("Digite a seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

# Processamento
idade = anoAtual - anoDeNascimento 
idadeSemanas = 4 * 12 * idade

# Saída
print(f" Sua idade é: {idade} ano(s)")
print(f" Sua idade em semanas: {idadeSemanas} semana(s)")