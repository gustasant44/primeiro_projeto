lista = ['banana' , 'maça', 'banana']




def add_fruta(a, b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("limão", "sorvete")

def del_fruta():
    lista.pop()
    print(lista)

del_fruta()    

for x in lista: 
    print(f"Esta fruta está na lista {x}")
