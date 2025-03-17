#Funciones con interactuando con variables globales.
#Ejemplo de como una funcion puede ejecutar el incremento de una variable Global
#En este concepto es importante que se esta empezamos a utilizar la expresion de la palabra reservada 'global'
#Es importante este detalle porque si no, no se utilizara la palabra en cuestion debido a que lamentablemente el programa pensara
#Buscara como su fuese una variable que ya deberia haber sido definida.

print('---> Alcance de Variables <---')

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # incrementamos la variable global
    contador_global += 1
    # incrementar la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias vece la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')

