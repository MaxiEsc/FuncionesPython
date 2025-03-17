#Funciones recursiva: Como en los demas lenguajes de programacion es una funcion que se llama asi misma.
# Basicamente es una funcion que debe avanzar a un caso base de lo contrario. estara en ciclos infinitos

print('---> Imprimir del 1 al 5 de forma recursiva <---')

# definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' --> ')  # 1
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Detalle interesante de las funciones recursivas Son las 'llamadas pendientes'
# A quese refiere con esta idea es que las funciones estran en si mismas y que dan en espera con el valor enviado en esa
# llamada anterior por lo que en este caso la funcion en la primera llamada quedara:
# funcion_recursiva(10) --> primera llamada
# funcion_recursiva(9) --> segunda llamada
# funcion_recursiva(8) --> tercera llamada
# funcion_recursiva(7) --> cuarta llamada
# funcion_recursiva(6) --> quinta llamada
# funcion_recursiva(5) --> sexta llamada
# funcion_recursiva(4) --> septima llamada
# funcion_recursiva(3) --> octava llamada
# funcion_recursiva(2) --> novena llamada
# funcion_recursiva(1) --> decima llamada y llego al caso base paso siguiente, Empezara a imprimir las llamadas anteriores
# Pendientes por lo que es interesante como se ejecuta ya que ya se terminaron de cumplir el caso base de las funciones.

# Programa principal
funcion_recursiva(10)