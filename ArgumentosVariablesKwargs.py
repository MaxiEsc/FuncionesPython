# *args - arguments - tupla
# **kwargs - keyword arguments (key,value) como un diccionario
print('---> Argumentos variables en forma de dict <---')

# El orden es si o si prioritario a respetar primero el '*args' y luego el '**kwargs' el uso del asteristico es solo para la declaracion de la funcion
def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamarmos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armandura','Playboy', edad=45)

# Es opcional enviar argumentos variables, al igual que los argumentos variables args es totalmente opcional utilizarlos.
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')
