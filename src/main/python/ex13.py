#Objetivo: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#Autor: Victor M

print("Digite o salário do funcionário: ")
salario = float(input())

bonus = salario * 15 / 100
salariobonus = salario + bonus

print("O salário do funcionário era: R${:.2f}, com aumento de 15%, ficou R${:.2f}".format(salario,salariobonus))