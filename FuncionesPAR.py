#Con este ejercicio vamos a comprobar nuevamente la idea de modulo como se hizo anteriormente en ejercicio anterior de funciones

print('----> Funcion par <----')

# Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Llamamos a la funcion #Como en un anterior ejercicio del tema pasado vamos a usar este archivo como modulo
# Pero aqui dejamos un Main improvisado para realizar pruebas algunas
if __name__ == '__main__':
    numero = int(input('Proporciona un valor numérico: '))
    print(f'Número par? {es_par(numero)}')

