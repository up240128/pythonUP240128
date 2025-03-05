#1 Encuentra la longitud del conjunto it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)
print('La longitud del conjunto de compañias es: ',len(it_companies))

#2 Añade 'Twitter' a it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print(it_companies)

#3 Insertar varias empresas de TI a la vez en el conjunto it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Mercado libre')
it_companies.add('Tesla')
it_companies.add('Hp')
it_companies.add('Dell')
it_companies.add('Lenovo')
print(it_companies)

#4 Eliminar una de las empresas del conjunto it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.remove('Google')
print(it_companies)

#5 ¿Cuál es la diferencia entre eliminar y descartar?
# La diferencia entre eliminar y descartar es que si el elemento que se quiere eliminar no se encuentra en el conjunto
# y se utiliza el metodo remove, se generará un error, mientras que si se utiliza el metodo discard no generará error.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.discard('Google')
print(it_companies)

##LEVEL 2
#1 Unir A y B
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
st2.isdisjoint(st1)
print(st1.union(st2))

#2 Encuentra la intersección A y B
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
st2.intersection(st1)
print(st1.intersection(st2))

#3 Es un subconjunto de B
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
st2.issubset(st1)
print(st1.issubset(st2))

#4 ¿Son A y B conjuntos disjuntos?
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
st2.isdisjoint(st1)
print(st1.isdisjoint(st2))

#5 Unir A con B y B con A
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
print(st1.union(st2))
print(st2.union(st1))

#6 ¿Cuál es la diferencia simétrica entre A y B?
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
print(st1.symmetric_difference(st2))

#7 Eliminar los conjuntos por completo
st1 = {'Mango', 'Pera', 'Limon', 'Naranja'}
st2 = {'Queso', 'Leche', 'Yogurt'}
st1.clear()
st2.clear()
print(st1)

##LEVEL 3
#1 Convierte las edades en un conjunto y compara la longitud de la lista y el conjunto, ¿cuál es más grande?
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades = set(edades)
print(edades)
print(len(edades))
print(len(edades) < len(edades))
