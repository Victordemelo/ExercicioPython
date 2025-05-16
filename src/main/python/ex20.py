# Objetivo: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# Autor: Victor M

from random import shuffle

print('Primeiro Aluno: ')
nome1 = str(input())
print('Segundo Aluno: ')
nome2 = str(input())
print('Terceiro Aluno: ')
nome3 = str(input())
print('Quarto Aluno: ')
nome4 = str(input())

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('A ordem de sorteados foi {}'.format(lista))
