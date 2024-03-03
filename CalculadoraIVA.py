

objetos = []
IVA= 0.21
precioTotal=0
#Funciones para agregar un objeto al array y calcular el IVA
def agregarObjeto(nombre, precio):
    objeto = {
        "nombre": nombre,
        "precio": precio,
        "iva": calcularIVA(precio),
        "precioTotal": precio+calcularIVA(precio)
    }
    objetos.append(objeto)

def calcularIVA(precio):
    return precio*IVA

#Iteración para agregar objetos al array
while True:
    objeto=str(input("Ingrese el nombre del objeto (exit para salir): "))
    if objeto.lower()=="exit":
        break
    precio=float(input("Ingrese el precio del objeto: "))
    agregarObjeto(objeto, precio)

#Iteración para imprimir los objetos y calcular el precio total
print("Objetos   ||  Precio   ||   IVA   ||   Precio Total")
for objeto in objetos:
    print(f"{objeto['nombre']}  ||  {objeto['precio']}  ||  {objeto['iva']}  ||  {round(objeto['precioTotal'],2)} s€")
    precioTotal+=objeto['precioTotal']
print("El precio total de los objetos es: ", round(precioTotal,2),"€")
