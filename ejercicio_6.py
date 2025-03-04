#1 Crear una tupla vacía
empty_tuple = ()
empty_tuple = tuple()

#2 Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
tpl = ('Renata', 'Roger', 'Santy', 'Ximena')
print('Mis hermanos son:', tpl)

#3 Unir tuplas de hermanos y hermanas y asignarlas a hermanos
tpl1 = ('Renata', 'Roger', 'Santy')
tpl2 = ('Ximena', 'Mateo', 'Nick')
tpl3 = tpl1 + tpl2
print(tpl3)

#4 ¿Cuántos hermanos tienes?
hermanos = ('Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick')
len(hermanos)
print('Los hermanos que tengo son: ',len(hermanos))

#5 Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
hermanos = ('Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick')
papis = ('Alejandra', 'René')
family_members = hermanos + papis
print('Los integrantes de mi falia son los siguientes: ', family_members)

##NIVEL 2

#1 Desempaquetar hermanos y padres de family_members
family_members= ('Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick', 'Alejandra', 'René')
all_family_members = family_members[6:8]    # all items
print(all_family_members)
family_members1= ( 'Alejandra', 'René', 'Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick')
all_family_members1 = family_members1[2:8]    # all items
print(all_family_members1)

#2 Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
frutas = ('fresa', 'mango ', 'sandia' , 'guayaba')
verdura = ('lechuga', 'jitomate', 'pepino', 'cebolla')
animales = ('leche', 'carne', 'huevo', 'manteca')
food_stuff_tp = frutas + verdura + animales
print(food_stuff_tp)

#3 Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
food_stuff_lt = ('fresa', 'mango ', 'sandia', 'guayaba', 'lechuga', 'jitomate', 'pepino', 'cebolla', 'leche', 'carne', 'huevo', 'manteca')
food_stuff_lt = list(food_stuff_lt)
print(food_stuff_lt)

#4 Extraiga el elemento o los elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt
food_stuff_tp = ('fresa', 'mango ', 'sandia', 'guayaba', 'lechuga', 'jitomate', 'pepino', 'cebolla', 'leche', 'carne', 'huevo', 'manteca')  
all_items = food_stuff_tp[0:12]         # all items
all_items = food_stuff_tp[0:]         # all items
middle_two_items = food_stuff_tp[0:4] +  food_stuff_tp[8:12]
print('La lista modificada queda asi: ', middle_two_items)   

#5 Separa los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
food_stuff_lt = ['fresa', 'mango ', 'sandia', 'guayaba', 'lechuga', 'jitomate', 'pepino', 'cebolla', 'leche', 'carne', 'huevo', 'manteca']
lista1 = food_stuff_lt[0:3]
lista2 = food_stuff_lt[9:12]
print(lista1)
print(lista2)

#6 Eliminar la tupla food_staff_tp por completo
lista = ('fresa', 'mango ', 'sandia', 'guayaba', 'lechuga', 'jitomate', 'pepino', 'cebolla', 'leche', 'carne', 'huevo', 'manteca')
del lista
print('La lista fue eliminada')

#7 Comprueba si un elemento existe en una tupla:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries
print('Estonia' in nordic_countries)

#7.1 Comprueba si un elemento existe en una tupla:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Iceland' in nordic_countries
print('Iceland' in nordic_countries)