

peso=float(input("Escribe tu peso (kg): "))
estatura=float( input("Escribe tu estatura (m): "))    
IMC= peso / (estatura**2)

print("Tu IMC (Indice de Masa Corporal) es de : ", round(IMC,2))
if(IMC<18.5):
    print("Estas bajo de peso")
elif(IMC>=18.5 and IMC<24.9):
    print("Tu peso es normal")
elif(IMC>=25 and IMC<29.9):
    print("Tienes sobrepeso")
else:
    print("Obesidad");
