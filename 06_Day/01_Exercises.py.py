#1 Crear una tupla vacía
empty_tuple = ()
empty_tuple = tuple()

#2 Crea una tupla que contenga los nombres de tus hermanas y tus hermanos (los hermanos imaginarios están bien)
tpl = ('Renata', 'Roger', 'Santy', 'Ximena')
print('Mis hermanos son:', tpl)

#3 Unir tuplas de hermanos y hermanas y asignarlas a hermanos
tpl1 = ('Renata', 'Roger', 'Santy')
tpl2 = ('Ximena', 'Mateo', 'Nick')
tpl3 = tpl1 + tpl2
print(tpl3)

#4 ¿Cuántos hermanos tienes?
hermanos = ('Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick')
len(hermanos)
print('Los hermanos que tengo son: ',len(hermanos))

#5 Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a family_members
hermanos = ('Renata', 'Roger', 'Santy', 'Ximena', 'Mateo', 'Nick')
papis = ('Alejandra', 'René')
family_members = hermanos + papis
print('Los integrantes de mi falia son los siguientes: ', family_members)
#REVISADO
print("Revisado")