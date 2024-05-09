import csv 

# with operador que va a operar un archivo 
#           ventas 1 es el excel csv
# para saver si es un directorio     "r"=leer, es read para saver si es un directorio
                           # as= nombrando al arcivo

                           
with open (r"D:\DiegoPyMiercoles\ArchivosMier\ventasMiercoles.csv", "r") as archivo:
    datos_csv=csv.DictReader(archivo)
    for fila in datos_csv:
        print(fila)

# resivir una ruta, del csv


# ejemplo 
fila = {}
print(fila)

fila["id"] = 8
print(fila)