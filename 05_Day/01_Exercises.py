#1 Declarar una lista vacía
lst = list()
print(len(lst))

#2 Declarar una lista con más de 5 elementos
lista = ['fresa', 'mango', 'pepino', 'uva', 'guayaba']
print('Los elementos que tienen son: ', len(lista))
print ('La lista de los elementos es la siguiente: ', (lista)) 

#3 Encuentra la longitud de tu lista
print('La longitud de la lista es: ', len(lista))

#4 Obtener el primer elemento, el elemento del medio y el último elemento de la lista.
fruits = ['fresa', 'mango', 'pepino', 'uva', 'guayaba']
fruits[0] = 'fresa'       
fruits[3] = 'pepino'      
fruits[4] = 'guayaba' 
print(fruits)    
print('El siguiente orden son los elementos principales, del centro y el ultimo: ', fruits[0], fruits[3], fruits[4])

#5 Declara una lista llamada mixed_data_types, coloca tu(nombre, edad, altura, estado civil, dirección)
mixed_data_types = ['Dariana', '18', '1.75', 'soltera', 'Calle de los gallos']
print('La lista de mis datos son: ', mixed_data_types)

#6 Declare una variable de lista llamada it_companies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print ('Las compañias de it son: ', it_companies)

#7 Imprima la lista usando print()
print ('Las compañias de it son: ', it_companies)

#8 Imprima el número de empresas en la lista
print ('El numero de empresas que hay en la lista es: ', len(it_companies))

#9 Imprima la primera, la segunda y la última empresa.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas[0] = 'Facebook'       
empresas[3] = 'Apple'      
empresas[6] = 'Amazon' 
print(empresas)    
print('El siguiente orden son los elementos principales, del centro y el ultimo: ', empresas[0], empresas[3], empresas[6])

#10 Imprima el listado después de modificar una de las empresas
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas [1] = 'Amazon'
empresas [0] = 'Microsoft'
print ('Las empresas modificadas son: ', empresas) 

#11 Añadir una empresa de TI a it_companies
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Samsung', 'Hp', 'Mercado libre']
print ('Las empresas modificadas son: ', empresas) 

#12 Insertar una empresa de TI en el medio de la lista de empresas
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Samsung', 'Hp', 'Mercado libre', 'intel']
empresas [5] = 'Hp'
print ('Las empresas modificadas son: ', empresas) 

#13 Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)
empresas = 'Facebook' + ' ' + ' ' + 'Google'  + ' ' + 'Microsoft' + ' '  + 'Apple' + ' ' +  'IBM' + ' ' +  'Oracle'  + ' ' +  'Amazon'
print( empresas.upper())  

#14 Unir it_companies con una cadena '#; '
empresas = 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'
print('#; '.join(empresas))

#15 Comprueba si una determinada empresa existe en la lista it_companies.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('temu in empresas', 'temu' in 'empresas')
print('CocaCola in empresas', 'CocaCola' in 'empresas')

#16 Ordena la lista en orden ascendente  
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(sorted(empresas))             

#17 Invierta la lista en orden descendente utilizando el método reverse()
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas.sort()
print(empresas)             
empresas.sort(reverse=True)
print(empresas) 

#18 Separa las primeras 3 empresas de la lista.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
empresas.pop(6)
empresas.pop(5)
empresas.pop(4)
empresas.pop(3)
print(empresas)

#19 Elimina las últimas 3 empresas de la lista.
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
empresas.pop(6)
empresas.pop(5)
empresas.pop(4)
print(empresas)

#20 Elimina de la lista las empresas de TI intermedias
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas.remove('Microsoft')
empresas.remove('Apple')
empresas.remove('IBM')
print(empresas)

#21 Eliminar la primera empresa de TI de la lista
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
empresas.pop(0)
print(empresas)

#22 Eliminar la o las empresas de TI intermedias de la lista
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
empresas.pop(3)
print(empresas)

#23 Eliminar la última empresa de TI de la lista
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
empresas.pop(6)
print(empresas)

#24 Eliminar todas las empresas de TI de la lista
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas.remove('Facebook')
empresas.remove('Google')
empresas.remove('Microsoft')
empresas.remove('Apple')
empresas.remove('IBM')
empresas.remove('Oracle')
empresas.remove('Amazon')
print(empresas)

#25 Destruir la lista de empresas de TI
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
empresas.pop(6)
empresas.pop(5)
empresas.pop(4)
empresas.pop(3)
empresas.pop(2)
empresas.pop(1)
empresas.pop(0)
print(empresas)

#26 Únete a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#27 Después de unir las listas en la pregunta 26. Copie la lista unida y asígnela a una variable full_stack, luego inserte Python y SQL después de Redux.
Unir_listas = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
nueva_lista = Unir_listas.copy()
nueva_lista.insert(5, 'Python') #insertar elemento en la quinta posicion
nueva_lista.insert(6, 'SQL') #insertar elemento en ls sexta posicion
print("La lista con Python y SQL incluidos es:",nueva_lista)

#REVISADO
print("Revisado")