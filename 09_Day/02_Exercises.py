#1 Escriba un código que califique a los estudiantes según sus puntuaciones
calestudiantes = float(input('La calificacion del estudiante es: '))
if calestudiantes > 80 and calestudiantes <= 100 :
    print("Tu calificacion es (A)")
if calestudiantes >= 70 and calestudiantes <= 89 :
    print("Tu calificacion es (B)")
if calestudiantes >= 60 and calestudiantes <= 69:
    print("Tu calificacion es (C)")
if calestudiantes >= 50 and calestudiantes <= 59:
    print ("Tu calificacion es (D)")
if calestudiantes >= 0 and calestudiantes <= 49:
    print ("Tu calificacion es (F)")

#2 Comprueba si la temporada es otoño, invierno, primavera o verano. Si el usuario introduce: septiembre, octubre o noviembre, la temporada es otoño. Diciembre, enero o febrero, la temporada es invierno. Marzo, abril o mayo, la temporada es primavera. Junio, julio o agosto, la temporada es verano.
mes = str(input('ingresa un mes: '))
verano = 'Junio, julio, agosto'
otono = 'septiembre, octubre, noviembre'
invierno = ' Diciembre, enero, febrero'
primavera = 'Marzo, abril, mayo'
if mes in verano:
    print('La estacion es verano')
elif mes in otono:
    print ('La estacion es otono')
elif mes in invierno:
    print ('La estacion es invierno')
elif mes in primavera:
    print('La estacion es primavera')

#3 La siguiente lista contiene algunas frutas:
listafrutas =  'banana', 'orange', 'mango', 'lemon'
fruta1 = 'fresa'
fruta2 = 'sandia'
fruta3 = 'banana'
if fruta2 in listafrutas:
    print('las frutas se encuentra en la lista: ', listafrutas , fruta2)
elif fruta1 in listafrutas:
    print('La fruta no se encuentra en la lista: ',listafrutas, fruta1)
elif fruta3 in listafrutas:
    print ('La fruta no se encuentra: ',listafrutas, fruta2)


   
