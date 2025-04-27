#Objetivo: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#Autor: Victor M

print("Digite a primeira nota do aluno: ")
n1 = float(input())
print("Digite a segunda nota do aluno: ")
n2 = float(input())

media = (n1+n2) / 2

print("A primeira nota foi: {:.1f}\nA segunda nota foi: {:.1f}".format(n1, n2))
print("A média do aluno foi: {:.1f}".format(media))