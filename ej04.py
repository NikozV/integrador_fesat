#Clase Libro
class Libro():
    def __init__(self, titulo, autor, precio, stock):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock
    
    #Creo los metodos
    def mostrar_libro(self):
        return f"""
        
        LIBRO
        Titulo : {self.titulo}
        Autor : {self.autor}
        Precio : {self.precio}
        Stock : {self.stock}
        
        """
    
    def actualizar_libro(self, nuevo_titulo, nuevo_autor, nuevo_precio, nuevo_stock):
        self.titulo = nuevo_titulo
        self.autor = nuevo_autor
        self.precio = nuevo_precio
        self.stock = nuevo_stock   

#Instancias
libro1 = Libro("Zelda - Ocarina of time", "Akira Himekawa", 2000, 15)
libro2 = Libro("El Silmarillión", "J.R.R. Tolkien", 2700, 2)

#Mostrar datos de los libros
print(libro1.mostrar_libro())
print(libro2.mostrar_libro())

#Cambiar dato de un libro
libro1.actualizar_libro("Batman - Condenado", "Lee Bermejo", 3500, 1)
print(libro1.mostrar_libro())