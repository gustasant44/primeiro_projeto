def escolher_time(numero_matricula):
    if numero_matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARAELO")


numero = int(input("digite o número de matricula: "))
escolher_time(numero)