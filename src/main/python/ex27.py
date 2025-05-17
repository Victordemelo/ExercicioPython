# Objetivo: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Autor: Victor M

print("Digite o seu nome: ")
nome = str(input()).strip()

nome_dividido = nome.split()

pri_nome = nome_dividido[0]
ult_nome = nome_dividido[-1]

print('Prazer em te conhecer !')
print('Primeiro nome: {}'.format(pri_nome))
print('Ultimo nome: {}'.format(ult_nome))
