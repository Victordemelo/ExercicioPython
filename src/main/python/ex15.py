#Objetivo: Escrever um programa que pergunte a quantidade de Km percorridos por um carro alugado, e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
#Autor: Victor M

print("Quantos dias o carro foi alugado? ")
dias = int(input())
print("Quantos Km, você percorreu com o carro alugado? ")
km = float(input())

carrodias = dias * 60
carrokm = km * 0.15

carrototal = carrodias + carrokm

print("O valor total a pagar pelo aluguel do carro será: R${:.2f}".format(carrototal))

