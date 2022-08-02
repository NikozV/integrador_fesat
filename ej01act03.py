#Creo Lista de compras vacia
lista_compras = []

#Agrego 5 productos a la lista
for i in range(5):
    lista_compras.append(input(f"Ingrese el {i+1}º producto a la lista de compras: "))

#Muestro la lista
print("-------------------------")
print("LISTA DE COMPRAS")
for lista in lista_compras:
    print (f" - {lista}")
    