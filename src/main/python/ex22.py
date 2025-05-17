# Objetivo: Crie um programa que leia o nome completo de uma pessoa e mostre, O nome com todas as letras maiúsculas e minúsculas, Quantas letras ao todo (sem considerar espaços), Quantas letras tem o primeiro nome.
# Autor: Victor M
print('Digite o seu nome: ')
n = str(input()).strip()

n_maius = n.upper()

n_minus = n.lower()

ler_total = n.replace(" ", "")
n_total = len(ler_total)

ler_prime = n.split()
n_prime = len(ler_prime[0])

print('O nome digitado foi: {}'.format(n))
print('Maiusculo: {}'.format(n_maius))
print('Minusculo: {}'.format(n_minus))
print('Total de caracteres: {}'.format(n_total))
print('Total de caracteres do primeiro nome: {}'.format(n_prime))
