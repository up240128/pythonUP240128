#1 Declare la función add_two_numbers . Esta función acepta dos parámetros y devuelve una suma.
def full_name ():
    first_name = 'Dariana'
    last_name = 'Villalpando'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
full_name () # calling a function

def add_two_numbers ():
    num_one = 1
    num_two = 8
    total = num_one + num_two
    print(total)
add_two_numbers()

#2 El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule área_del_círculo .
def areaDelCirculo ():
    radio = float(input('ingresa un radio'))
    area = 3.1416 * radio **2
    print(area)
areaDelCirculo()

#3 Escriba una función llamada add_all_nums que tome cualquier número de argumentos y los sume. 
# Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) 
print(sum_of_numbers(100))

#4 La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32.
#  Escriba una función que convierta °C a °F, convert_celsius_to-fahrenheit .
def convert_celsius_to_fahrenheit():
    C = float(input('Ingresa una temperatura en grados Celsius: '))
    Farehreit = (C * 9/5) + 32
    print('La temperatura en grados Farehreit es: ', Farehreit)
convert_celsius_to_fahrenheit()

#5 Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
def check_season():
    mes = str(input('ingresa un mes: '))
    verano = 'junio, julio, agosto'
    otono = 'septiembre, octubre, noviembre'
    invierno = ' diciembre, enero, febrero'
    primavera = 'marzo, abril, mayo'
    if mes in verano:
        print('La estacion es verano')
    elif mes in otono:
        print ('La estacion es otono')
    elif mes in invierno:
        print ('La estacion es invierno')
    elif mes in primavera:
        print('La estacion es primavera')
check_season()

#6 Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal
def calculate_slope():
    x1 = float(input('Ingresa un valor para la pendiente: '))
    y1 = float(input('Ingresa un valor para la pendiente: '))
    x2 = float(input('Ingresa un valor para la pendiente: '))
    y2 = float(input('Ingresa un valor para la pendiente: '))
    m = (y2-y1)/(x2-x1)
    print ('La pendiente es: ', m)
calculate_slope()

#7 La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. 
# Escriba una función que calcule el conjunto solución de una ecuación cuadrática, solve_quadratic_eqn 
def solve_quadratic_eqn():
    a = float(input('Ingresa un valor para a: '))
    b = float(input('Ingresa un valor para b: '))
    c = float(input('Ingresa un valor para c: '))
    x = float(input('Ingresa un valor para x: '))
    ecu = (a*x**2) + (b*x) + c
    print('El valor de la ecuacion cuadratica es: ', ecu)
solve_quadratic_eqn()

#Declara una función llamada print_list. Esta toma una lista como parámetro e imprime cada elemento de la lista.

