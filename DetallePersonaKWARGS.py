#En este caso tenemos que un ejemplo donde podemos ver el funcionamiento de los kwargs aplicado a una estructura de datos
#complejo como es la ejemplo de las caracteristica basica de una persona.

print('---> Imprimir detalles de una persona usando kwargs <----')

# Funcion que acepta argumentos variables en forma de llave-valor dict
# En este caso utilizamos un funcion de para iterar kwargs con el concepto de umpacking con llave y valor
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')