# Objetivo: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
# Autor: Victor M

print('Digite o nome de uma cidade: ')
cidade = str(input()).strip()

cidade_min = cidade.lower()
verificação = cidade_min[:5] == 'santo'

print(verificação)

