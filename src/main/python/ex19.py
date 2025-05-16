# Objetivo: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# Autor: Victor M

from random import choice

print("Primeiro Aluno: ")
a1 = str(input())
print("Segundo Aluno: ")
a2 = str(input())
print("Terceiro Aluno: ")
a3 = str(input())
print("Quarto Aluno: ")
a4 = str(input())

lista = [a1, a2, a3, a4]
sorteio = choice(lista)

print("O aluno escolhido foi: {}".format(sorteio))
