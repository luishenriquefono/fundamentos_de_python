# Solicite a temperatura para o usuário. Se a temperatura estiver abaico de 16 fraus, informe ao usuário para pegar uma blusa.Ao final escreva fim do programa.


print("Algoritmo para informar se o usuário deve pegar uma blusa ou não ")

print() #pular linha

#Entrada Solicitar a temperatura para o usuário
temperatura = int( input("Digite a temperatura: ") )

print() #pular linha

#Processameento
if temperatura <= 16 : #true
    print("Pegue e coloque uma blusa pois está frio")

else : #false
    print(" Não precisa pegar uma blusa pois está calor")

print() #pular linha
print("Fim do programa")
