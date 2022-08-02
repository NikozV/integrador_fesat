#Funcion que convierte de Dolar a Peso Argentino
def de_dolar_a_peso(dolar):
    return dolar * 200

#Pido al usuario que ingrese los dolares
dolar_u = float(input("Ingrese los dolares: "))
pesos = de_dolar_a_peso(dolar_u)

pesos_redondeados = round(pesos, 2)

#Muestro en pantalla el resultado
print(f"Los {dolar_u} US$ a Pesos Argentinos es: {pesos_redondeados}$AR")