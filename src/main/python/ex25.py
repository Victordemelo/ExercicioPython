# Objetivo: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# Autor: Victor M

print('Digite o seu nome: ')
nome = str(input()).strip()

nome_lower = nome.lower()
procurar = 'silva' in nome_lower

print('Seu nome tem silva? {}'.format(procurar))
