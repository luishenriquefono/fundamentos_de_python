# Solicite a temperatura para o usuário. Se a temperatura estiver abaico de 16 fraus, informe ao usuário para pegar uma blusa.Ao final escreva fim do programa.


print("Algoritmo para informar se o usuário deve pegar uma blusa ou não ")

#Entrada Solicitar a temperatura para o usuário
temperatura = int( input("Digite a temperatura: ") )

print() #pular linha

#Processameento
if temperatura <= 16 :
    print("Pegue e coloque uma blusa pois está frio")

print() #pular linha
print("Fim do programa")


