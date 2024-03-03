#Aplicación funcional de diccionarios
#Crear un programa que pida una cadena de texto y devuelva un diccionario 
# con cada palabra que contiene y sus repeticiones.


cadena= str(input("Ingrese una cadena de texto: "))
words={}
def crearDiccionario(cadena):
    for word in cadena.split():
        if word in words:
            words[word]+=1
        else:
            words[word]=1
    return words
def wordMostRepeated(words):
    max=0
    for word in words:
        if words[word]>max:
            max=words[word]
            wordMostRepeated=word
    return wordMostRepeated

print(crearDiccionario(cadena))
print(wordMostRepeated(words))
