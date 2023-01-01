'''
    En este archivo se describe cómo trabajar con excepciones.
'''

try:
    print('Intentando correr el código contenido en el try')
except:
    print('No se pudo ejecutar el código contenido en el try')
    print('Ejecutando el contenido del except')
else:
    print('No existieron excepciones')
    print('Ejecutando el código contenido en el else')
finally:
    print('Se corrió el código correspondiente de la excepción')
    print('Corriendo el código contenido en el finally')