'''
    En este archivo se describen funciones importantes para los objetos
    de tipo String.
'''

#Variable de prueba.
string = 'HelloWorld'

#Imprime toda la cadena en mayúsculas.
print(string.upper())

#Imprime toda la cadena en minúsculas.
print(string.lower())

#Cambia las mayúsculas por minúsculas (no viceversa).
print(string.lower())

#Cambia la primera letra de la primera palabra a mayúscula.
print(string.capitalize())

#Cambia las el la cadena del primer parámetro por la del segundo parámetro.
print(string.replace('Hello', 'Bye'))

#Cuenta la cantidad de caracteres que conforman un string. Retorna un entero.
print(string.count('o'))

#Comprueba se el parámetro se encuentra al inicio del string. Retorna un booleano.
print(string.startswith('Hello'))

#Comprueba se el parámetro se encuentra al final del string. Retorna un booleano.
print(string.endswith('World'))

#Retorna una lista por cada elemento encontrado antes de el parámetro (separador). Retorna una lista.
print(string.split(' '))

#Retorna la posición de donde empieza el parámetro. Retorna un entero.
print(string.find('ello'))

#Retorna la longitud del string. Retorna un entero.
print(len(string))

#Retorna el índice del primer elemento que coincide con el parámetro. Retorna un entero.
print(string.index('l'))

#Accedemos al elemento que se encuentra en el índice solicitado.
print(string[0])

#Retorna True si todos los valores son caracteres numérics (0-9).
print(string.isnumeric())

#Retorna True si todos los caracteres son letras del alfabeto (a-z).
print(string.isalpha())


''' FORMAS DE IMPRIMIR POR PANTALLA '''

#Variables de prueba.
name = 'Agustín Óscar'

print('Hello my friend ' + str(name))
print(f'Hello my friend {name}')
print('Hello my friend {}'.format(name))