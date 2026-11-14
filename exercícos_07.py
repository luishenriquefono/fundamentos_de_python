# 7. Receba nome, cargo e salário e acrescente 10%.

# Entrada
nome = input(" Digite o seu nome: ")
Cargo = input(" Digite o seu cargo: ")
salario = float(input(" Digite o seu salário: "))

# Processamento
salarioAumento = salario * 1.10


# Saída
print(f" nome:{nome}")
print(f" Cargo: {Cargo}")
print(f" salário com aumento de 10%: {salarioAumento: .2f}")