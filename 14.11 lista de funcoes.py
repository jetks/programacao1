def quantofalta (n1, n2):
    if nota1<0 or nota2<0:
        return
    else:
        soma = (-nota1-nota2 + 0)+21
        soma= float(soma)
        return (soma)


soma1=0   
nota1 = float(input())
nota2 = float(input())
soma1 = quantofalta(nota1, nota2)



while nota1<0 or nota2<0:
    soma1=0
    print("valor inavalido")
    nota1 = float(input())
    nota2 = float(input())
    soma1 = quantofalta(nota1, nota2)
    
if soma1 >0:
    print ("Faltam %1.d pontos" % (soma1))
elif soma1<=0 :
    soma1=soma1*-1
    print ("Você está aprovado, você tem  %.d pontos sobrando" % (soma1))
