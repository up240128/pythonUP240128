#1 Obtener la información del usuario mediante input(“Ingrese su edad:”). Si el usuario tiene 18 años o más, indique: Tiene edad suficiente para conducir. Si es menor de 18 años, indique que espere los años que falatan. 
edad = float(input('Ingrese su edad: '))
if edad > 18:
    print('Tiene edad suficiente para conducir')
elif edad < 18:
    print('Espere los años que faltan')
else:
    print('tiene edad suficiente para conducir')

#2 Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad:”) para obtener la edad como entrada. Puedes usar una condición anidada para imprimir "año" si hay una diferencia de edad de 1 año, "años" si la diferencia es mayor y un texto personalizado si my_age = your_age. Salida:
edad = float(input('Ingrese su edad: '))
tu_edad = float(input('Ingrese su edad: '))
diferencia = (edad - tu_edad)
if edad > tu_edad :
    print('Eres mayor por: ', edad)
elif edad < tu_edad:
    print('Eres menor por:', edad)
else:
    edad == tu_edad
    print('tenemos la misma edad')

#3 Obtener dos números del usuario mediante la solicitud de entrada. Si a es mayor que b, devuelve a mayor que b; si a es menor que b, devuelve a menor que b; de lo contrario, a es igual a b. Salida:
A = float(input('Ingrese un numero: '))
B = float(input('Ingrese un numero: '))
if A > B :
    print("El primer numero es mayor al segundo")

if A > B :
    print("El segundo numero es mayor al segundo")
if A == B :
    print ("Los numeros son los mismos")