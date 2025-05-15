#Objetivo: Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.
#Autor: Victor M

import math

print("Digite um numero: ")
n1 = float(input())

n_inteiro = math.trunc(n1)

print("O número digitado foi: {}, e o numero inteiro dele é: {}".format(n1, n_inteiro))