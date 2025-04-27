#Objetivo: Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Autor: Victor M

#Primeira linha comentada para mostrar o cifrão ao lado da mensagem, para o usuário nao confundir e botar o cifrão.

#print("Quantos de dinheiro você tem na carteira, para comprar dólares e euros?") 
dinheiro = float(input("Quantos de dinheiro você tem na carteira, para comprar dólares e euros? R$"))

dolar = dinheiro / 5.69
euro = dinheiro / 6.49

print("Com R${:.2f}, voce pode comprar US${:.2f}, e {:.2f} em euros.".format(dinheiro,dolar,euro))