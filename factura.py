class Factura:
    __numero_factura = 0
    def __init__(self, cliente):
        Factura.__numero_factura += 1
        self.__numero = Factura.__numero_factura
        self.__cliente = cliente
        self.__total = 0
        self.__lineas = {}

    def numero(self):
        return self.__numero

    def cliente(self):
        return self.__cliente

    def lineas(self):
        return self.__lineas

    def producto(self):
        return self.__producto

    def ayadir_producto(self, producto, cantidad):
        self.__lineas[producto.codigo()] = f'{producto.denominacion()} Cantidad: {cantidad}, Precio: {producto.precio() * cantidad} €'
        self.__total += producto.precio() * cantidad

    def borrar_productos(self, producto):
        del self.__lineas[producto]

    def total_factura(self):
        return self.__total

    def imprimir_factura(self):
        print(f'Nº FACTURA: {self.__numero} CLIENTE: {self.__cliente.nombre()} {self.__cliente.apellidos()}')
        print("ARTICULOS:")
        for clave, valor in self.__lineas.items():
            print(f'Producto: {clave}, {valor}')
        print(f'Total factura: {self.total_factura()} €')
