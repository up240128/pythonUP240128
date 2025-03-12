##LEVEL 3
#1 Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades = set(edades)
print(edades)
print(len(edades))
lista1 = {22, 19, 24, 25, 26, 24, 25, 24}
lista2 = {22, 19, 24, 25, 26, 24, 25, 24}
lista2.symmetric_difference(lista1) 
lista1.symmetric_difference(lista2)
print(lista2.symmetric_difference(lista1))
print(lista1.symmetric_difference(lista2))  #No hay diferencia entre la longitud de la lista y el conjunto

#2 Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto.
print('Cadena: Es una secuencia de caracteres, se representa entre comillas simples o dobles.') 
print('Tupla: Es una colección ordenada e inmutable de elementos, se representa entre parentesis.')
print('Conjunto: Es una colección no ordenada y no indexada de elementos, se representa entre llaves.')
print('Lista: Es una colección ordenada y mutable de elementos, se representa entre corchetes.')

#3 Soy profesor y me encanta inspirar y enseñar a la gente. ¿Cuántas palabras únicas se han utilizado en la oración? Utilice los métodos de división y de configuración para obtener las palabras únicas.
frase1 = 'Soy profesor y me encanta inspirar y enseñar a la gente'
frsemod = frase1.split()
print("Las palabras en la oracion son:", len(set(frsemod)))
print ("Las palabras en la oracion son:", frsemod)