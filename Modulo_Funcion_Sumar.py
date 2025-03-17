#En este ambito se va ha estudiar los modulos en cuestion de los archivos
#Es crear como un acceso con pequeños codigos funcionales.

# Definimos la funcion Sumar(num a, num b) --> num c
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

#Para realizar las pruebas dentro del archivo se debe escribir el siguiente codigo
if __name__ == '__main__':
    print(f'Imprimir Prueba de la funcion desde el modulo: {sumar(15,36)}')
