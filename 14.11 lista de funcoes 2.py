def IMC (v1,v2):
    imc = peso/(altura**2)

    return imc

peso = float(input("Peso: "))
altura = float(input("Altura: "))

fun = IMC(peso,altura)

if 16 <= fun <= 16.9:
    print ("Muito abaixo do peso")

elif 17 <= fun <= 18.4:
    print ("Abaixo do peso")

elif 18.5 <= fun <= 24.9:
    print ("Peso normal")

elif 25 <= fun <= 29.9:
    print ("Acima peso")

elif 30 <= fun <= 34.9:
    print ("Obesidade Grau I")

elif 35 <= fun <= 40:
    print ("Obesidade Grau II")

elif fun >= 40:
    print ("Obesidade Grau III")
