#Objetivo: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#Autor: Victor M

import math

print("Digite o cateto oposto: ")
oposto = float(input())
print("Digite o cateto adjacente: ")
adjacente = float(input())

triangulo = math.hypot(oposto, adjacente)

print("O cateto oposto é: {}, o cateto adjacente é: {}, e a hipotenusa é {:.2f}".format(oposto, adjacente, triangulo))