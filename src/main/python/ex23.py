# Objetivo: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Autor: Victor M

print('Digite um número de 0 a 9999: ')
n = str(input()).zfill(4)

u = n[3]
d = n[2]
c = n[1]
m = n[0]

print('O número digitado foi: {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
