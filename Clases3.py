#crear un sistema de gestión de inventario
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print("Se agregó el producto ", producto.nombre, "al inventario :)")
    
    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print("Se eliminó el producto ", producto.nombre, "del inventario")
                return
        print("El producto con nombre", nombre, "no se encontró en el inventario.")
    
mi_producto1 = Producto("Galleta Oreo", 2.50, 20)
mi_producto2 = Producto("Jugos del valle", 1.50, 25)
mi_producto3 = Producto("Piqueos grande", 6, 15)

mi_inventerio = Inventario()

mi_inventerio.agregar_producto(mi_producto1)
mi_inventerio.agregar_producto(mi_producto2)
mi_inventerio.agregar_producto(mi_producto3)

mi_inventerio.eliminar_producto("Jugos del valle")