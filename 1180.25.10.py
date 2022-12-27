qte = int(input())
lista = input().split(" ")

posicao = 0
menor = lista[0]
cont = 0

for kkj in lista:
    if(kkj < menor):
        menor = kkj
        posicao = cont
    cont += 1
    
print("Menor valor: %d" %(menor))
print("Posicao: %d" %(posicao))
