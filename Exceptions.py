#Corregir si el usuario introduce un valor que no sea entero
"""
while True:
    try:
        edad= int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("Por favor, introduce un valor entero")

if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
"""
# Otra manera de hacerlo con funciones y recursión
    
def solicitar_edad(message=""):
    try:
        print(message)
        return int(input("Introduce tu edad: "))
    except ValueError:
        return solicitar_edad(message="Por favor, introduce un valor entero")

edad= solicitar_edad()
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

"""
Tipos de excepciones:  
    TypeError: Error cuando no es una cadena
    KeyError: Error de clave en los diccionarios
    IndexError : Error de índice en los arrays
    NameError: Error de variable no definida
    RunTimeError: Error de ejecución
    ValueError : Error de valor
    ZeroDivisionError : Error de división por cero

Ejemplo para varias excepciones:
    try:
        int(...)
    except (ValueError, TypeError):
        print("Error")
    except ZeroDivisionError:
        print("Error de división por cero")
    except:
        print("Error no controlado")
    finally:
        print("Se ejecuta siempre")
"""

#Lanzar excepciones

def sumar(a,b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("Ambos valores deben ser enteros")
    return a+b

#Crear excepciones personalizadas
"""
    Para crear una excepción personalizada, se debe crear una clase que herede de Exception
"""
class ErrorEnDivision(Exception):
    def __init__(self, mensaje):
        self.mensaje= mensaje