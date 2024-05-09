import Operaciones_lic as ol  # ol es alias
ruta = r"D:\DiegoPyMiercoles\ArchivosMier\ventasMiercoles.csv"
nueva_venta = { 
        "id" : 0,
        "codigo_cliente": 10009,
        "cliente": "Gabriel Casas",
        "producto":"Papas fritas",
        "precio": 68,
        "descuento": "",
        "iva": ""
}

# ol.registrar_csv(nueva_venta, ruta)

# mientras la lectura sea verdadera vamos a seguir leyendo 
lectura = True
while lectura:
    accion = input('Accion:  ')
    if (accion == 'nuevo'):
        # leer los procuttos
        codigo_cliente = input('Codigo Cliente:')
        cliente = input('Cliente:')
        producto = input('Producto:')
        precio = input('Precio:')

        nueva_venta = {
            'id': 0,
            'codigo_cliente': codigo_cliente,
            'cliente': cliente,
            'producto': producto,
            'precio': precio,
            'descuento': '',
            'iva': ''
        }
        Operaciones_lic.registrar_csv(nueva_venta, ruta)
    else:
        lectura = False
        # break
# en el resultado sale:
# Accion: nuevo 


