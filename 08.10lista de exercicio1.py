inscritos = input().split(" ")
compareceram = input().split(" ")

insc = []
comp = []

for nome in compareceram:
    if nome in inscritos:
        insc.append(nome)
    else:
        comp.append(nome)

print(insc)
print(comp)

compareceram.sort()
print(compareceram)
