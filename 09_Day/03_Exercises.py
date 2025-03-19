# 1 Compruebe si el diccionario de la persona tiene la clave de habilidades; de ser así, imprima la habilidad intermedia en la lista de habilidades
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    print ('Las habilidades se encuentran en la lista', person['skills'])

#2 Verifique si el diccionario de la persona tiene la clave de habilidades; de ser así, verifique si la persona tiene la habilidad 'Python' e imprima el resultado.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python esta en la lista de habilidades')

#3 Si una persona tiene habilidades solo JavaScript y React, imprima ('Es un desarrollador front-end')
#  imprima ('título desconocido'): para obtener resultados más precisos, se pueden anidar más condiciones.
if 'skills' in person:
    if 'JavaScrip' and 'React' in person ['skills']:
        print('Es un desarrollador front-end')

# 4 si la persona tiene habilidades Node, Python, MongoDB, imprima ('Es un desarrollador backend')
if 'skills' in person:
    if 'node' or 'python' and 'MogoDB' in person ['skills']:
         print('Es un desarrollador backend')

#5 si la persona tiene habilidades React, Node y MongoDB, Imprima ('Es un desarrollador completo'), de lo contrario






