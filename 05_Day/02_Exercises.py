##NIVEL 2
#1 La siguiente es una lista de 10 estudiantes por edades:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#1.1 Ordena la lista y encuentra la edad mínima y máxima.
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('La edad minima es:', ages[0])
print('La edad maxima es:', ages[-1])

#1.2 Agregue la edad mínima y la edad máxima nuevamente a la lista
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('La edad minima es:', ages[0])
print('La edad maxima es:', ages[-1])
ages.append(ages[0])
ages.append(ages[-1])
print(ages)

#1.3 Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
suma = 24 + 24
print ('La edad media es:', suma/2)

#1.4 Encuentra la edad promedio (suma de todos los elementos dividida por su número)
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
sumaedades = 19 + 19 + 20 + 22 + 24 + 24 + 24 + 25 + 25 + 26
promedio = sumaedades/10
print ('la edad promedio es :', promedio)

#1.5 Encuentra el rango de edades (máximo menos mínimo)
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
edades.sort()
rango = edades[-1] - edades[0]
print('El rango de edades es:', rango)

#1.6 Compare el valor de (mín - promedio) y (máx - promedio), use el método abs()
edades = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
edades.sort()
promedio = 23 #El promdeio que marac en realidad es de 22.8 pero por este motivo lo dejare en 23 porque se acerca mas a este valor por los decimales
min_promedio = abs(edades[0] - promedio)
max_promedio = abs(edades[-1] - promedio)
print('El valor de (min - promedio) es:', min_promedio)
print('El valor de (max - promedio) es:', max_promedio)

#2 Encuentre el pais o los paises intermedios de la lista
import paises as p
countries = p.countries
countries.sort()
print(countries)
print('El pais intermedio es:', countries[96])

#3 Dividir la lista de países en dos listas iguales si es par o no hay un país más para la primera mitad.
import paises as p
countries = p.countries
print (len(countries))
all_countries = countries[97:193]
print('LA LISTA UNO ES LA SIGUIENTE: ', all_countries)
print('           ')
all_countries1 = countries[98:193]
print('LA LISTA DOS ES LA SIGUIENTE: ', all_countries1)

#4 ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']. Desglose los primeros tres países y el resto como países escandinavos.
paises1 = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
all_paises1 = paises1[2:6]
print('Los primeros tres paises son:', paises1[0:3])
print('Los paises escandinavos son:', all_paises1)