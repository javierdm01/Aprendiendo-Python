#Ejercicio Con Listas o Arrays
# Crear un programa que pida la nota de 5 asignaturas y calcule la media de todas ellas

asignatures= ["matematicas", "fisica", "quimica", "historia", "lengua"]
ratings=[]

for asignature in asignatures:
    rating= float(input(f"¿Cual es tu nota en {asignature}? : "))
    ratings.append(rating)

print(ratings)
print("Tu nota media de las asignaturas es :", sum(ratings)/len(ratings))