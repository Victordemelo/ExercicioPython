#Objetivo: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Autor: Victor M

import math

print("Digite o valor de um angulo: ")
angulo = float(input())

angulo_radiano = math.radians(angulo)
sen = math.sin(angulo_radiano)
cos = math.cos(angulo_radiano)
tan = math.tan(angulo_radiano)

print("O ângulo de {} tem o seno de {:.2f}".format(angulo, sen))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angulo, cos))
print("O ângulo de {} tem a tangente de {:.2f}".format(angulo, tan))