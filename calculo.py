# Função para gerar a tabuada de um número
def tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicita ao usuário um número
numero = int(input("Digite um número para ver a tabuada: "))

# Chama a função para exibir a tabuada
tabuada(numero)
