'''
    En este archivo de describen las principales estructuras de datos
    así como sus métodos.
'''


'''
    LISTAS

    Son vectores de longitud variable.
'''

#Declaración.
protocolos = ['ftp', 'ssh', 'smtp']

#Agregar un elemento a la lista.
protocolos.append('http')

#Ordenar la lista.
protocolos.sort()

#Obtener la longitud de la lista.
len(protocolos)

#Obtener la posición en que se encuentra un elemento específico.
position = protocolos.index('ssh')
print('La posición de SSH es: ' + str(position))

#Remover un elemento específico de la lista.
protocolos.remove('ssh')
print(protocolos)

#Eliminar el último elemento de la lista. También se le puede
#pasar como parámetro el índice del elemento que se desea eliminar.
protocolos.pop()
protocolos.pop(0)
print(protocolos)

#Limpiar completamente la lista.
protocolos = ['ftp', 'ssh', 'smtp', 'http']
protocolos.clear()
print(protocolos)

#Invertir el orden de la lista.
protocolos = ['ftp', 'ssh', 'smtp', 'http']
protocolos.reverse()

#Recorrer una lista.
print('Recorriendo la lista con for:')
protocolos = ['ftp', 'ssh', 'smtp', 'http']
for protocol in protocolos:
    print(protocol)

#Trabajar directamente con las posiciones de la lista.
print('Modificando un elemento específico de la lista:')
protocolos = ['ftp', 'ssh', 'smtp', 'http']
protocolos[0] = 'dns'
print(protocolos)

#Crear una lista desde m hasta n-1 con valores enteros.
#range(m, n)
ports = list(range(1,100))
print(ports)

#Utilizar una condicional para validar si un elemento está dentro de una lista.
if 'dns' in protocolos:
    print('Se ejecutan las instrucciones porque dns está dentro de la lista.')

if 'telnet' not in protocolos:
    print('Estas instrucciones se ejecuta porque no existe telnet en la listas')

#Comprobar todos los métodos que contiene el objeto.
print(dir(protocolos))

#Otra forma de encontrar un elemento en una lista.
toFind = 'smtp' #Elemento a buscar.
found = False #Bandera de encontrado.

for i in range(len(protocolos)):
    if protocolos[i] == toFind:
        print('Elemento encontrado en el índice:' + str(i))


'''
    TUPLAS

    Son listas las cuales no pueden cambiar su tamaño ni su contenido.
'''

#Declaración.
protocolsTuple = ('ftp', 'ssh', 'smtp')

try:
    protocolsTuple[0] = 'http'
    protocolsTuple.append('http')
except:
    print('Error: No se puden modificar las tuplas')

print(dir(protocolsTuple))


'''
    DICCIONARIOS

    Permiten asociar valores a claves. Se puede acceder al valor de una clave a
    través de un operador índice
'''

#Declaración.
protocolsDiccionary = {
    'nombre': 'ftp',
    'puerto': 21
}

#Unificación de diccionarios.
services = {'ftp':21, 'ssh':22}
services_bk = {'smtp':25, 'ftp':21}
services.update(services_bk)
print(services)

#Obtener todas las claves como lista.
print(services.keys())

#Obtener todos los valores como una tupla.
print(services.values())

#Iterar los elementos de un diccionario.
for key, value in services.items():
    print(key, value)