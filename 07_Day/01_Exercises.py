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




