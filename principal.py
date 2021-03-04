from cliente import Cliente
from factura import Factura
from articulo import Articulo

rosa = Cliente('24571259K', 'Rosa', 'González')

factura1 = Factura(rosa)

televisor = Articulo(100, 'Televisor', 399)
targeta_grafica = Articulo(101, 'Targeta Grafica', 239)

factura1.ayadir_producto(televisor, 2)
factura1.ayadir_producto(targeta_grafica, 1)

factura1.imprimir_factura()
