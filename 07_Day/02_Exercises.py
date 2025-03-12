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