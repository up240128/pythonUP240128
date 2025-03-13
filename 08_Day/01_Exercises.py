#1 Crea un diccionario vacío llamado perro
empty_dict = {}
dct = {'perro'}
print(dct)

#2 Añade nombre, color, raza, patas y edad al diccionario de perros
empty_dict = {}
dct = {'perro'}
dct = {'perro':'value1'}
dct['lola'] = 'value2'
dct['negro'] = 'value3'
dct['pug'] = 'value4'
dct['4'] = 'value5'
dct['3'] = 'value6'
print(dct)

#3 Cree un diccionario de estudiantes y agregue nombre, apellido, género, edad, estado civil, habilidades, país, ciudad y dirección como claves para el diccionario.
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)

#4 Obtenga la longitud del diccionario del estudiante
print(len(person))

#5 Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print('first anem' in dct)

#6 Modifique los valores de las habilidades agregando una o dos habilidades
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Sofia'
person['age'] = 22
person['country'] = 'texas'
print (person)

#7 Obtenga las claves del diccionario como una lista
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
keys = person.keys()
print (keys)

#8 Obtener los valores del diccionario como una lista
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
values = person.values()
print(values)     

#9 Cambie el diccionario a una lista de tuplas usando el método items()
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.items())

#10 Eliminar uno de los elementos del diccionario
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('age')
person.pop('last_name')
print(person)

#11 Eliminar uno de los diccionarios
person = {
    'first_name':'Dariana',
    'last_name':'Villalpando Duron',
    'age':18,
    'country':'Aguscalientes',
    'is_married':False,
    'skills':['Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
animales = {'perro', 'gato', 'vaca','gallo', 'leon'}
del person
print(animales)
