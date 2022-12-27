def fatorial (num):
    resultado = 1

    for i in range(1, num+1):
        resultado *= i

    return resultado

n = int(input())
fat = fatorial(n)

print (fat)

