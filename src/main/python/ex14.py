#Objetivo: Escreva um programa que converta um temperatura digitada em °C para °F.
#Autor: Victor M

print("Digite a temperatura em °C: ")
c = float(input())

f = (c*1.8) + 32

print("A temperatura em °C está {:.1f}, e em °F está {:.1f}".format(c,f))