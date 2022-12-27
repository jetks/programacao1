cifras = input().split(" ")
raul = input().split(" ")

quant = len(cifras)
cont1 = 0
cont2 = 0

for i in range(quant):
    if raul[i] == cifras[i]:
        cont2 += 1
        
    else:
        if cont2 > cont1:
                cont1 = cont2
                cont2 = 0

if cont2 > cont1:
    cont1 = cont2

print(cont1)

