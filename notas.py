media = int(input("insira a média do aluno"))



if media <= 0:
    print(f"olá Gustavo! >> MÉDIA INVÁLIDA. ABAIXO DO PERMITIDO << ")

elif media < 6:
    print(f"olá Gustavo! Sua média é: {media}, você está de recuperação!")

elif media ==7 :
    print(f"olá, Gustavo! Sua média é: {media}, você tirou REGULAR!")

elif media == 10: 
    print(f"olá, Gustavo! Sua média é: {media}, você tirou EXELENTE!")   
elif media < 10:    
     print(f"olá, Gustavo! Sua média é: {media}, você tirou BOM!")
