print("\n Bienvenido al restaurante UPO")

# clase base #
class MenuItem:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self):
        return f"{self.nombre} - ${self.precio:,}"

# subclases #
class Bebida(MenuItem):
    def __init__(self, nombre, sabor, precio):
        super().__init__(nombre, precio)
        self.sabor = sabor
    
    def mostrar(self):
        return f"{self.nombre} ({self.sabor}) - ${self.precio:,}"

class Perro(MenuItem):
    pass

class Hamburguesa(MenuItem):
    pass

class Picada(MenuItem):
    pass

# clase orden #
class Orden:
    def __init__(self):
        self.items = []  # aqui guardamos el producto y la cantidad)

    def agregar(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def mostrar(self):
        print("\n--- Detalle de la orden ---")
        total = 0
        for producto, cantidad in self.items:
            subtotal = producto.precio * cantidad
            print(f"{cantidad} x {producto.nombre} = ${subtotal:,}")
            total += subtotal
        print(f"\nTOTAL A PAGAR: ${total:,}")
        return total

# menu #
menu = [
    Bebida("Jugo Hit", "Frutos Tropicales", 2500),
    Bebida("Jugo Hit", "Mango", 2500),
    Bebida("Jugo Hit", "Piña-Naranja", 2500),
    Bebida("Gaseosa Postobon", "Uva", 2500),
    Bebida("Gaseosa Postobon", "Manzana", 3000),
    Bebida("Coca-Cola", "Clásica", 4000),
    Bebida("Coca-Cola", "Zero", 4000),

    Perro("Perro Sencillo", 8000),
    Perro("Perro Especial", 10000),
    Perro("Perro Ranchero", 12000),
    Perro("Perro Extremo", 15000),

    Hamburguesa("Hamburguesa Sencilla", 12000),
    Hamburguesa("Hamburguesa Especial", 15000),
    Hamburguesa("Hamburguesa Doble Carne", 18000),
    Hamburguesa("Hamburguesa Todo Terreno", 23000),

    Picada("Picada Sencilla", 13000),
    Picada("Picada Doble", 15000),
    Picada("Picada Mixta", 17000),
    Picada("Picada Mega", 20000)
]

# programa #
while True:
    print("\n========= MENÚ =========")
    for i, item in enumerate(menu, start=1):
        print(f"{i}. {item.mostrar()}")

    print("Escribe 'fin' para terminar el pedido")
    print("Escribe 'salir' para cerrar el programa")

    orden = Orden()

    while True:
        opcion = input("\n Elige un número del menu: ")

        if opcion.lower() == "fin":
            orden.mostrar()
            break
        elif opcion.lower() == "salir":
            print("Gracias por visitarnos ")
            exit()
        elif opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= len(menu):
                cantidad = int(input("¿Cuántas unidades deseas?: "))
                producto = menu[opcion - 1]
                orden.agregar(producto, cantidad)
                print(f"Agregado: {cantidad} x {producto.nombre}")
            else:
                print("error, intenta de nuevo.")
        else:
            print("error, escribe un número o 'fin'.")

    otra = input("\n¿Deseas hacer otro pedido? (si/no): ").lower()
    if otra != "si":
        print(" Gracias por tu compra ")
        break
