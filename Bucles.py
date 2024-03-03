# Multiplicar tu nombre tantas veces como indiques con diferentes bucles
nombre= str(input("Ingrese su nombre: "))
numero= int(input("Ingrese el número de repeticiones: "))

print("Con for")
for i in range(numero):
    print(nombre)

print("Con while")
while numero>0:
    print(nombre)
    numero-=1

