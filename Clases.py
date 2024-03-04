#Ejercicio de clases para practicar la herencia entre clases
#Este ejercicio se basa en la creacion de dos clases, una clase padre y una clase hija
# La clase padre es Poligono, la cual tiene dos atributos, base y altura 
# La clase hija es Rectangulo y el Triangulo, las cuales heredan de la clase padre Polígono

class Poligono:
    """
    Define un poligono segun su base y su altura.
    """
    def __init__(self, b ,h):
        self.b=b
        self.h=h

class Rectangunlo(Poligono):
    def area(self):
        return self.b*self.h

class Triangulo(Poligono):
    def area(self):
        return (self.b*self.h)/2
    

Rectangunlo= Rectangunlo(20,10)
Triangulo= Triangulo(20,12)



print("El area del triangulo es: ", Triangulo.area())
print("El area del rectangulo es: ", Rectangunlo.area())