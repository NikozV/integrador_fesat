#Diccionario de productos
productos_marketplace = {"Computadora": 60000, "Mouse": 1500, "Teclado": 2000, "Auriculares": 3500, "Monitor": 20000}

#Lista de las compras y total gastado
carrito = []
total = 0

#MENU de opciones
while True:
    print("""
    BIENVENIDOS AL MARKETPLACE DE FESAT ELIJA UNA OPCION: 

        1.	Ver los productos
        2 .	Comprar un producto
        3.	Ver mi carrito
        4.	Salir

    """)
    opcion = int(input("Ingrese una opción: "))
    #print(opcion)

    #Ver productos
    if opcion == 1:
        print("\n -- PRODUCTOS EN STOCK -- \n")
        
        for producto, valor in productos_marketplace.items():
            
            print(f"PRODUCTO: {producto} PRECIO: ${valor} \n")
        input("\n - Toque una tecla para continuar...")
    
    #Comprar un producto        
    elif opcion == 2:
        compra = input("Elija el producto a comprar: \n")
        carrito.append(compra)
        total += productos_marketplace[compra]
        productos_marketplace.pop(compra)
        input("\n - Toque una tecla para continuar...")
    
    #Ver mi carrito
    elif opcion == 3:
        if carrito == []:
            print("\n CARRITO VACIO")
            input("\n - Toque una tecla para continuar...")
        else:
            print("\n SUS PRODUCTOS EN EL CARRITO SON: \n")
            print(f"PRODUCTO: {carrito} PRECIO: ${total} \n")
            input("\n - Toque una tecla para continuar...")

    #Salir
    elif opcion == 4:
        print("\n -- GRACIAS POR USAR LA APLICACION -- \n")
        exit()
    #Error en la eleccion del producto
    else:
        print("\n -- OPCION INCORRECTA, VUELVA A INTENTAR --")
        input("\n - Toque una tecla para continuar...")