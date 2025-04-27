#Objetivo: Fazer um programa que leia um número inteiro e mostrar na tela o seu sucessor e o seu antecessor.
#Autor: Victor M

print("Digite um número: ")
n = int(input())

sucessor = n+1
antecessor = n-1

print("O número digitado foi {}, o sucessor é {}, e o antecessor é {}.".format(n, sucessor, antecessor))