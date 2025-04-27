#Objetivo: Escrever um programa que leia um valor em metros e o exiba, convertendo em centímetros e milímetros.
#Autor: Victor M

print("Digite uma distancia em metros: ")
metros = float(input())

kilometro = metros/1000
hectometro = metros/100
decametro = metros/10
metros = metros
decimetros = metros*10
centimetros = metros*100
milimetros = metros*1000

print("O valor digitado em metros foi: {:.2f}".format(metros))
print("O valor em kilometros: {:.2f}, O valor em hectometro: {:.2f}, O valor em decametro {:.2f}".format(kilometro,hectometro,decametro))
print("O valor em decimetros: {:.2f}, O valor em centimetros: {:.2f}, O valor em milimetros {:.2f}".format(decimetros,centimetros,milimetros))

