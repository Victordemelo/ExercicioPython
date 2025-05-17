# Objetivo:  Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# Autor: Victor M

print("Digite uma frase qualquer: ")
frase = str(input()).strip()

frase_maius = frase.upper()
contar = frase_maius.count('A')
aparece_pri = frase_maius.find('A')
aparece_ult = frase_maius.rfind('A')

print('A frase tem {} "A" '.format(contar))
print('A primeira vez que aparece o "A" é no: {}'.format(aparece_pri + 1))
print('A ultima vez aparece o "A" é no: {}'.format(aparece_ult + 1))
