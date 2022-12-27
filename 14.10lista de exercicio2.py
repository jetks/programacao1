cifras = input().split(" ")
raul = input().split(" ")

quant = len(cifras)
cont = 0

for i in range(quant):
    if raul[i] == cifras[i]:
        cont += 1
        
porcentagem = cont / quant * 100
print("%.1f %%" % (porcentagem))
