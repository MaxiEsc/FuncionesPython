#Retorno de lo argumentos
#Como en la mayoria de los lenguajes Pytho0n mantiene la estetica posicional de los argumentos en cuestion.
#Pero Python Posee una caracteristica destacada qeu permite pasar los argumento por nombre no por la posicion

print('---> Funcion con argumentos por nombre <---')

#En este caso dentro de funcion establecemos los valores por default es interesantes porque apellido y edad poseen valores por default pero nombre no.
def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Ricardo', 'Quintana', 32)
# Llamar la funcion usando argumentos por nombre

#En este caso pasamos los argumentos por numbre asignados con un valor definido y se aplicara en los demas llamados
imprimir_persona(nombre='Carlos', apellido='Rojas', edad=28)
# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden por lo que no importa su orden
imprimir_persona(edad=28, apellido='Rojas', nombre='Carlos')
# Argumentos con valor por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos', apellido='Rojas')
imprimir_persona(apellido='Rojas', nombre='Carlos')

