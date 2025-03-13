sentence = '30 dias de python'
print(sentence)
frase = 'Codificación para todos'
print(frase)
empresa = 'codificacion para todos'
print(empresa)
##Imprima la longitud de la cadena de la empresa utilizando el método len() y print() .
print('La longitud de la palbra es: ', len(empresa))

 ##Palabrras a mayusculas 
challenge = 'thirty days of python'
print(challenge.upper()) 
challenge = 'codificacion para todos'
print(challenge.upper()) 

##Palabras a minusculas
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.lower()) 
challenge = 'CODIFICACION PARA TODOS'
print(challenge.lower())

##Métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
challenge = 'thirty days of python'
print(challenge.title()) 
challenge = 'codificacion para todos'
print(challenge.title())
challenge = 'thirty days of python'
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
challenge = 'codificacion para todos'
print(challenge.capitalize()) # 'Thirty days of python'
challenge = 'coficacion para todos'
print(challenge.swapcase())   # CODIFICACION PARA TODOS
challenge = 'Codificacion Para Todos'
print(challenge.swapcase())  # CODIFICACION PARA TODOS

##Recortar (cortar) la primera palabra de la cadena Codificación para todos
language = 'Codificación para todos'
print(language[12:24]) # Codificación

##Compruebe si la cadena Codificación Para Todos contiene una palabra Codificación 
challenge = 'Codificación para todos'
print(challenge.find('Codificación'))  # 0 este numero aparece cuando la a palabra se encuentra en el texto
print(challenge.find('helado')) # -1 este numero aparece cuando no se encuentra la palabra

##Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python
challenge = 'codificación para todos'
print(challenge.replace('codificación para todos', 'python')) # 'python'

##Cambie Python para todos a Python para todos utilizando el método de reemplazo
challenge = 'python para todos'
print(challenge.replace('python para todos', 'python')) # 'python para todos'

##Divida la cadena 'Coding For All' usando el espacio como separador (split())
challenge = 'Coding For All'
print(challenge.split()) 

##Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma
challenge = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(challenge.split())

##Cuál es el carácter en el índice 0 en la cadena Codificación para todos
challenge = 'Codificación para todos'
print(challenge[0]) # C

##Cuál es el último índice de la cadena Codificación Para Todos
challenge = 'Codificación para todos'
print(challenge[-1]) #s

##Cuál es el carácter en el índice 10 en la cadena Codificación para todos
challenge = 'Codificación para todos'
print(challenge[10]) # ó

##Crea un acrónimo o una abreviatura para el nombre 'Python para todos'
frase1 = 'python para todos'
acronymo = ''.join(word[2] for word in frase1.split())
print("La abreviacion de (python para todos) es:",acronymo)

##Cree un acrónimo o una abreviatura para el nombre 'Coding For All'
frase2 = 'Coding For All'
acronimo= ''.join(word[0] for word in frase2.split())
print("La abreviacion de (Coding For All) es:",acronimo)

##Utilice el índice para determinar la posición de la primera aparición de C en Codificación para todos.
challenge = 'Codificación para todos'
sub_string = 'C'
print(challenge.index(sub_string))  # 0

##Utilice el índice para determinar la posición de la primera aparición de F en Codificación para todos.
challenge = 'Codificación para todos'
sub_string = 'f'
print(challenge.index(sub_string))  # 4

##Utilice rfind para determinar la posición de la última aparición de l en Coding For All People.
challenge = 'coding for all people'
print(challenge.rfind('a'))  
challenge = 'coding for all people'
print(challenge.rfind('l'))

##Utilice index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
challenge = 'No puedes terminar una oración con porque porque porque es una conjunción'
sub_string = 'porque'
print(challenge.index(sub_string))  # 35

##Utilice rindex para encontrar la posición de la última aparición de la palabra porque en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
challenge = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(challenge.rfind('porque')) #49

##Elimina la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción' 
challenge = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(challenge.replace('No puedes terminar una oración con porque porque porque es una conjunción', 'No puedes terminar una oración con es una conjunción'))

##Encuentra la posición de la primera aparición de la palabra 'porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción'
challenge = 'No puedes terminar una oración con porque porque porque es una conjunción'
sub_string = 'porque'
print(challenge.index(sub_string))#35

##Elimina la frase 'porque porque porque' en la siguiente oración: 'No puedes terminar una oración con porque porque porque es una conjunción' 
challenge = 'No puedes terminar una oración con porque porque porque es una conjunción'
print(challenge.replace('No puedes terminar una oración con porque porque porque es una conjunción', 'No puedes terminar una oración con es una conjunción'))

##''Coding For All' comienza con una subcadena Coding 
frasesita = 'Coding For All'
print ('la frase de la variable frasesita comienza con la palabra Coding:', frasesita.startswith('Coding'))

##'Coding For All' termina con una subcadena 'coding 'frasesita = 'Coding For All'
sentence = 'Coding For All'
print ('la frase de la variable sentence comienza con la palabra Coding:', sentence.endswith('Coding'))

##'Codificación para todos', elimina los espacios finales izquierdo y derecho en la cadena dada.
sentence1 = 'Codificaciónparatodos'
sentence1 = sentence1.strip()
print('La frase eliminando espacios es: ',sentence1)

##Cuál de las siguientes variables devuelve Verdadero cuando usamos el método isidentifier()?
##30 días de Python
##Treinta días de Python
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

##La siguiente lista contiene los nombres de algunas bibliotecas de Python: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Únase a la lista con un hash con una cadena de espacios.
language = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
Django,Flask,Bottle,Pyramid,Falcon = language 
print(Django) 
print(Flask) 
print(Bottle) 
print(Pyramid) 
print(Falcon) 

##Utilice la secuencia de escape de nueva línea para separar las siguientes oraciones.
'I am enjoying this challenge. I just wonder what is next.'
print('I am enjoying this challenge. \nI just wonder what is next.')

##Utilice una secuencia de escape de tabulación para escribir las siguientes líneas
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

##Utilice el método de formato de cadena para mostrar lo siguiente:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %d meters square.' % (radius, area))

##Realice lo siguiente utilizando métodos de formato de cadena:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8*6 = {8*6}")
print(f"8/6 = {8/6}")
print(f"8%6 = {2}")
print(f"8//6 = {1}")
print(f"8**6 = {262144}")


#REVISADO
print("Revisado")