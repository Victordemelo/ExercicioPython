#Objetivo: Fazer um algoritmo que irá ler o preço de um produto e mostrar o seu novo preço, com 5% de desconto.
#Autor: Victor M

print("Digite o preço do produto: ")
produto = float(input())

desc = (produto/100) * 5 # ou (produto*5) / 100
produtodesc = produto - desc

print("O valor do produto é R${:.2f}, com desconto de 5%, será R${:.2f}".format(produto, produtodesc))