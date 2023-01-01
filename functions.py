'''
    En este archivo se describe cómo crear y llamar funciones.
'''

#Función que determina si un valor se encuentra en una lista.
def contains(sequence, item):
    inside = False
    for element in sequence:
        if element == item:
            inside = True
            break
    return inside

#Función que determina si un valor se encuentra en una lista (simple).
def contains_simple(sequence, item):
        return item in sequence

print(contains_simple([100, 200, 300, 400], 200))


#Función para ingresar datos por teclado.
inputUser = input('Ingrese un número: ')
print(type(inputUser))

