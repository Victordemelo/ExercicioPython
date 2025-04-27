#Objetivo: Fazer um programa que leia a largura e a altura de uma parede em metros, calcular a sua área e a quantidade de tinta necessária para pintar-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#Autor: Victor M

print("Digite a Largura da parede: ")
largura = float(input())
print("Digite a Altura da parede: ")
altura = float(input())

area = largura * altura
tinta = area / 2

print("A sua parede tem {:.2f}x{:.2f}, a área dela é: {:.2f}m²".format(largura, altura, area))
print("Para pintar a parede, você ira precisar de {:.2f} Litros de tinta.".format(tinta))
