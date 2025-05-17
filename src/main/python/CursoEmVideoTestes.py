# Introdução ao Python#
# Autor: Victor M#


# Desafio 01#

# print("Digite o seu nome: ")
# nome = input()

# print("Olá", nome , "Prazer em te conhecer!")


# Desafio 02#

# print("Digite o dia do seu nascimento: ")
# dia = input()
# print("Digite o Mês do seu nascimento: ")
# mes = input()
# print("Digite o Ano do seu nascimento: ")
# ano = input()

# print("Seu aniversário é:" , dia, "/" , mes , "/" , ano)


# Desafio 03#

# print("Digite o primeiro numero: ")
# n1 = int(input())
# print("Digite o Segundo numero: ")
# n2 = int(input())

# soma = n1+n2
# print("A soma entre:", n1, "e", n2, "vale =" , soma)                   Python 2.0
# OU
# print("A soma entre {} e {} vale = {}".format(n1,n2,soma))              Python 3.0


# Desafio 04#
# print("Digite Algo: ")
# n = input()

# print("Alpha : ", n.isalpha())
# print("Numério: ", n.isnumeric())
# print("Alpha Numério: ", n.isalnum())


# Desafio 05#
# print("Digite um valor: ")
# n1 = int(input())
# print("Digite outro valor: ")
# n2 = int(input())

# s = n1+n2
# m = n1*n2
# d = n1/n2
# di = n1//n2
# exp = n1**n2

# print("A soma é {},\nA multiplicação é {}, \nA divisão é {:.3f}". format(s, m, d), end=" ")
# print("A divisão inteira é {}, a potência é {}".format(di, exp))


# Desafio 06#
# print("Digite um valor: ")
# n1 = int(input())
# print("Digite outro valor: ")
# n2 = int(input())

# soma = n1+n2
# sucessor = (n1+n2)+1
# antecessor = (n1+n2)-1

# print("O Valor da soma foi {}, o sucessor é {}, o antecessor é {}.".format(soma, sucessor, antecessor))


# Desafio 07#
# print("Digite um número: ")
# n1 = int(input())

# dobro = n1*2
# triplo = n1*3
# raiz = n1/(1/2)

# print("Número digitado foi: {}, o dobro do numero digitado: {}, o triplo: {}, e a raiz quadrada: {}.".format(n1, dobro, triplo, raiz))


# Desafio 08#
# print("Digite a primeira nota: ")
# nota1 = int(input())
# print("Digite a segunda nota: ")
# nota2 = int(input())

# media = (nota1+nota2) / 2

# print("A primeira nota foi: {}\nA segunda nota foi: {}\nA média do aluno foi: {}".format(nota1, nota2, media))


# Desafio 09#
# print("Digite o valor em metros: ")
# metros = float(input())

# centrimetros = metros * 100
# milimetros = metros * 1000

# print("O valor digitado em metros: {}\nO valor digitado em centímetros: {}\nO valor digitado em milímetros: {}".format(metros, centrimetros, milimetros))


# Desafio 10#
# print("Digite um numéro inteiro para fazer a tabuada: ")
# inteiro = int(input())

# um = 1*inteiro
# dois = 2*inteiro
# tres = 3*inteiro
# quatro = 4*inteiro
# cinco = 5*inteiro
# seis = 6*inteiro
# sete = 7*inteiro
# oito = 8*inteiro
# nove = 9*inteiro
# dez = 10*inteiro

# print("1 x {} = {}".format(inteiro,um))
# print("2 x {} = {}".format(inteiro,dois))
# print("3 x {} = {}".format(inteiro,tres))
# print("4 x {} = {}".format(inteiro,quatro))
# print("5 x {} = {}".format(inteiro,cinco))
# print("6 x {} = {}".format(inteiro,seis))
# print("7 x {} = {}".format(inteiro,sete))
# print("8 x {} = {}".format(inteiro,oito))
# print("9 x {} = {}".format(inteiro,nove))
# print("10 x {} = {}".format(inteiro,dez))


# Desafio 11#
# print("Digite quantos ($)Reais você tem em sua carteira: ")
# reais = float(input())

# dolar = reais / 3.27

# print("Você pode comprar {:.2f} em dólares.".format(dolar))


# Desafio 12#
# print("Digite a Largura da parede: ")
# largura = float(input())
# print("Digite a Altura da parede: ")
# altura = float(input())

# area = largura*altura
# litros = area / 2

# print("A Área da parede é {:.2f} m²".format(area))
# print("Será nescessário {:.2f} litros de tinta para pintar uma parede de {:.2f} m²".format(litros, area))


# Desafio 13#
# print("Digite o preço do produto: ")
# preco = float(input())

# desconto = (preco/100) * 5
# precodesc = preco - desconto


# print("O Valor do produto sem desconto é: {:.2f} R$, com o desconto fica {:.2f} R$".format(preco, precodesc))


# Desafio 14#
# print("Digite o seu salário: ")
# salario = float(input())

# bonus = (salario/100) * 15
# salariobonus = salario + bonus

# print("Parebéns, o seu salário de {:.2f}, sera aumentado para {:.2f}".format(salario, salariobonus))


# Desafio 15#

# import math;
# ou
# from math import sqrt


# print("Digite o numero para obter a raiz: ")
# raiz = int(input())

# raizquadrada = math.sqrt(raiz)

# print("A raiz quadrada é: {}".format(raizquadrada))


# Desafio 16#
# import math

# print("Digite um número real: ")
# real = float(input())

# conversor = math.trunc(real)

# print("O número real digitado foi {}, e a sua porção inteira é {}".format(real, conversor))


# Desafio 17#
# import math

# print("Digite o cateto oposto: ")
# oposto = float(input())
# print("Digite o cateto adjacente: ")
# adjacente = float(input())

# hipotenusa = math.hypot(oposto, adjacente)

# print("O cateto oposto é {}, o cateto adjacente é {}, e a hipotenusa do triângulo retângulo é: {}".format(oposto, adjacente, hipotenusa))


# Desafio 18#
# import math
# print("Digite um ângulo qualquer: ")
# angulo = float(input())

# angulo_radiano = math.radians(angulo)

# seno = math.sin(angulo_radiano)
# cosseno = math.cos(angulo_radiano)
# tangente = math.tan(angulo_radiano)

# print("O Ângulo em graus foi {}, e o seno é {}, cosseno é {}, e a tangente é {}".format(angulo, seno, cosseno, tangente))


# Desafio 19#
# import random

# print("Digite o nome dos quatro alunos")
# print("Aluno 01: ")
# aluno01 = input()
# print("Aluno 02:")
# aluno02 = input()
# print("Aluno 03: ")
# aluno03 = input()
# print("Aluno 04: ")
# aluno04 = input()

# lista = [aluno01, aluno02, aluno03, aluno04]

# sorteio = random.choice(lista)

# print("O aluno escolhido foi {}".format(sorteio))


# Desafio 20#
# import random
# print("Digite o nome dos quatro alunos")
# print("Aluno 01: ")
# aluno01 = str(input())
# print("Aluno 02:")
# aluno02 = str(input())
# print("Aluno 03: ")
# aluno03 = str(input())
# print("Aluno 04: ")
# aluno04 = str(input())

# lista = [aluno01, aluno02, aluno03, aluno04]

# random.shuffle(lista)

# print("A ordem dos alunos ficou: ")
# print(lista)


# Desafio 21#


# pygame.init()

# pygame.mixer.music.load('C:/Users/victor/Codigos_Programação/vscode/Python1/ExercicioPython/src/main/python/ex21.mp3')
# pygame.mixer.music.play()
# pygame.time.wait(180000)


# Códigos de exemplos

'''
frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
frase = '   Curso em Vídeo Python   '
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split()

print(dividido[2])
print(dividido[2][3])
'''


# Desafio 22#
# print('Digite o seu nome: ')
# nome = str(input())

# nome_maisculo = nome.upper()

# nome_minusculo = nome.lower()

# nome_espaco = nome.replace(" ", "")
# nome_letras = len(nome_espaco)

# dividir =  nome.split()
# letras_pri_nome = len(dividir[0])

# print('Nome Maísculo: {}'.format(nome_maisculo))
# print('Nome Minúsculo: {}'. format(nome_minusculo))
# print('Quantidade de letras no nome sem espaço: {}'.format(nome_letras))
# print('Quantas letras no primeiro nome: {}'.format(letras_pri_nome))




# Desafio 23#
'''
print('Digite um numero de 0 a 9999: ')
n = input().zfill(4)

n_unidade = n[3]
n_dezena = n[2]
n_centena = n[1]
n_milhar = n[0]

print('O Número digitado foi: {}'.format(n))
print('A Unidade é: {}'.format(n_unidade))
print('A Dezena é: {}'.format(n_dezena))
print('A centena é: {}'.format(n_centena))
print('O Milhar é: {}'.format(n_milhar))

#OU

print('Digite um numero de 0 a 9999: ')
n = int(input())

n_unidade = n // 1 % 10
n_dezena = n // 10 % 10
n_centena = n // 100 % 10
n_milhar = n // 1000 % 10

print('O Número digitado foi: {}'.format(n))
print('A Unidade é: {}'.format(n_unidade))
print('A Dezena é: {}'.format(n_dezena))
print('A centena é: {}'.format(n_centena))
print('O Milhar é: {}'.format(n_milhar))
'''




# Desafio 24#
'''
print('Digite um nome de uma cidade: ')
cidade = str(input())

cidade_lower = cidade.lower()
procurar = "santo" in cidade_lower

print('O nome da cidade digitado foi: {}'.format(cidade))
print('Tem "SANTO" no nome da cidade? {}'.format(procurar))
'''




# Desafio 25#
'''print('Digite o seu nome: ')
n = str(input())

print(n.find('Silva'))
'''




# Desafio 26#




# Desafio 27#
