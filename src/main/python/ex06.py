#Objetivo: Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#Autor: Victor M

print("Digite um valor: ")
valor = int(input())

dobro = valor*2
triplo = valor*3
raiz = valor**(1/2) #ou pow(valor, (1/2))

print("O valor digitado foi {}\nO dobro é {}\nO triplo é {}\nE a raiz é {:.2f}".format(valor,dobro,triplo,raiz))
