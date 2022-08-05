#Funciones de la calculadora

def suma (num1,num2):
    return num1 + num2
def resta (num1,num2):
    return num1 - num2
def multi (num1,num2):
    return num1 * num2
def div (num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return f"No se puede dividir por 0 (cero)"

#Menu y opciones

flag = True
while flag:
    while True:
        try:
            print ("""
                1. Sumar
                2. Restar
                3. Multiplicar
                4. Dividir
                5. Salir
            """)
            opcion = int(input("Ingrese una opcion de la calculadora: \n"))
            break
        except ValueError:
            print("ERROR - Solo numeros enteros -")

    if opcion >=1 and opcion <=4:
        while True:
            try:
                num_1 = float(input("Ingrese el primer numero: "))
                num_2 = float(input("Ingrese el segundo numero: "))
                break
            except ValueError:
                print("ERROR - Solo numeros -")

    if opcion == 1:
        print(f"\n{num_1} + {num_2} = {suma(num_1,num_2)}")
        input("\n - Toque una tecla para continuar...")
    elif opcion == 2:
        print(f"\n{num_1} - {num_2} = {resta(num_1,num_2)}")
        input("\n - Toque una tecla para continuar...")
    elif opcion == 3:
        print(f"\n{num_1} * {num_2} = {multi(num_1,num_2)}")
        input("\n - Toque una tecla para continuar...")
    elif opcion == 4:
        print(f"\n{num_1} / {num_2} = {div(num_1,num_2)}")
        input("\n - Toque una tecla para continuar...")
    elif opcion == 5:
        print("\n -- GRACIAS POR USAR LA APLICACION -- \n")
        flag = False
    else:
        print("\n -- OPCION INCORRECTA, VUELVA A INTENTAR --")
        input("\n - Toque una tecla para continuar...")
        