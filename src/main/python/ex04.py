#Objetivo: Fazer um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as inforções possíveis sobre ela. 
#Autor: Victor M

print("Digite algo: ")
n = input()

print("O item digitado foi {}".format(n))

print("O tipo primitivo44 foi: ", type(n))
print("Tem somente numeros?", n.isnumeric())
print("Tem somente letras?", n.isalpha())
print("É Alpha Numerico?", n.isalnum())
print("Tem espaço na palavra?", n.isspace())
print("É tudo minúsculo?", n.islower())
print("É tudo maiúsculo?", n.isupper())
