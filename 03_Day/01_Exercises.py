age=18
altura=1.75
print()
print (type(int(age)),'El valor de la edad es de clase: ', int, age) 
print (type(float(altura)),'El valor de la edad es de clase: ', float, altura) 
print('Numero complejo: ', 25j)

##Calcular el area de un triangulo
baseTriangulo = float(input('Ingrese la base del triangulo: '))
alturaTriangulo = float(input('Ingrese la altura del triangulo: '))
areaDelTriangulo = baseTriangulo * alturaTriangulo / 2
print('El area del triangulo es de: ', areaDelTriangulo)

##Calcular el perimetro de un triangulo
ladoATriangulo = float(input('Ingrese el lado a del triangulo: '))
ladoBTriangulo = float(input('Ingrese el lado b del triangulo: '))
ladoCTriangulo = float(input('Ingrese el lado c del triangulo: '))
perimetroTriangulo = ladoATriangulo + ladoBTriangulo + ladoCTriangulo
print('El perimetro del triangulo es de: ', perimetroTriangulo)

##Calcular longitud y ancho de un rectangulo
longitudRectangulo = float(input('Ingresa la longitud del rectangulo: '))
anchoRectangulo = float(input('Ingrese el ancho del rectangulo: '))

##Calcular area y perimetro del rectangulo
areaRectangulo = longitudRectangulo * anchoRectangulo
perimetroRectangulo = longitudRectangulo + anchoRectangulo + longitudRectangulo + anchoRectangulo
print ('El area del rectangulo es de: ', areaRectangulo)
print ('El perimetro del rectangulo es de: ', perimetroRectangulo)

##Area y circunferencia de un circulo
radio = float(input('ingresa el radio de un circulo: '))
diametro = radio * 2
areaDelCirculo = 3.1416* radio**2
print('El area del circulo es: ', areaDelCirculo)
circunferenciaDelCirculo = 3.1416 * diametro
print ('La circunferencia del circulo es de: ', circunferenciaDelCirculo)

##Pendiente de interseccion con el eje x and y
##Para calcular los ejes de interseccion se debe despejar en la ecuacion la x, y 
x = 0
yc=2*x-2
print("El valor de y es: ", yc)

y = 0
xc = (y + 2)/2
print("El valor de x es: ", xc)
print('El valor de la pendiente es: (' + str(xc) +' , '+ str(yc)+')')

## Encontrar la pendiente y y la distancia euclidiana entre el punto (2, 2) y el punto (6, 10).
x1 = 2
y1 =2
x2 = 6
y2 = 10
m = (y2-y1)/(x2-x1)
print ('La pendiente es: ', m)
d = ((x2 - x1)**2 + (y2 - y1)**2)
res = d**0.5
print ('La distancia euclidiana es de: ', res)

##Comparacion de las pendientes


## Calcula el valor de y (y = x^2 + 6x + 9). 
x = 0
y = x**2 + 6*x + 9
print ('El valor de la variabale y es: ', y)
xuno = 3
yuno = xuno**2 + 6*xuno + 9
print ('El valor de la variabale y es: ', yuno)
xdos = 5
ydos = xdos**2 + 6*xdos + 9
print ('El valor de la variabale y es: ', ydos)

##Logitud palabra
print('El numero de letras que tiene dragon es: ', len('dragon'))
print('El numero de letras que tiene python es: ', len('python'))  
print(len('dragon') != len('python'))  # False

##comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'
palabra1 = 'python'
palabra2 = 'drangon'
if 'on' in palabra1 and 'on' in palabra2:
    print("'on' se encuentra en ambos 'python' y 'dragon'")
else:
    print("'on' no se encuentra en ambos 'python' y 'dragon'")

##Utilice el operador in para comprobar si hay jerga en la oración.
frase1 = 'Espero que este curso no esté lleno de jerga'
print('jerga in Espero que este curso no esté lleno de jerga', 'jerga' in 'Espero que este curso no esté lleno de jerga')

##No hay "on" tanto en dragon como en python
print('ON in dragon', 'ON' in 'dragon')
print('ON in python', 'ON' in 'python')

#Longitud de la palabra python y convertir la variabale en flotante
palabras = 'python'
print('El numero de letras que tiene python es: ', len('python'))
print (type(float(len(palabras))))

##Los números pares son divisibles por 2 y el resto es cero
numero1 = 4
numero2 = 6
numero3 = 7
numero4 = 25
frase1 = 'Divisible entre 2'
frase2 = 'No es divisible entre 2 y el resultado es 0 '
sum = numero1/2
print('El numero es: ', frase1, sum )
sum2 = numero2/2
print('El numero es: ', frase1, sum2 )
sum3 = numero3/2
print('El numero es: ', frase2, 0)
sum4 = numero4/2
print('El numero es: ', frase2, 0)

##Comprueba si la división del piso de 7 por 3 es igual al valor int convertido de 2,7.
num = 7
div = 3
division = num/div
print(type(int(division)))
print('El resultado de la division no es 2,7: ', not True)
print('El valor de la division es: ', int(division))

##Comprueba si el tipo de '10' es igual al tipo de 10
print('El tipo de 10 es igual al tipo de 10: ', type(10) == type(10))

##Comprueba si int('9.8') es igual a 10
valor = '9.8'
print(type(float(valor)))
print('El valor del numero es: ', valor)
print('El valor de 9.8 es igual a 10: ', not True)

##Escriba un script que solicite al usuario que ingrese horas y tarifa por hora. ¿Cómo calcular el salario de la persona?
horas = float(input('Ingrese las horas trabajadas: '))
tarifa = float(input('Ingrese la tarifa por hora: '))
salario = horas * tarifa
print('El salario de la persona es de: ', salario)

##Escriba un script que solicite al usuario que ingrese la cantidad de años. Calcule la cantidad de segundos que puede vivir una persona. Suponga que una persona puede vivir cien años.
años = float(input('Ingrese la cantidad de años: '))
segundos = años * 365 * 24 * 60 * 60
print('La cantidad de segundos que puede vivir una persona es de: ', segundos)

