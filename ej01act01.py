#Funcion que convierte de Celsius a Fahrenheit
def de_c_a_f(celsius):
    return celsius * 1.8 + 32

#Pido al usuario que ingrese los grados en Celsius
celsius_u = float(input("Ingrese la temperatura en Cº: "))
fahrenheit = de_c_a_f(celsius_u)

#Muestro en pantalla resultado
print(f"La temeperatura ingresada {celsius_u}ºC a Fahrenheit es: {fahrenheit}ºF")