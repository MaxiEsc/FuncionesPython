#Este concepto de argumentos variables permiten que una funcino acepte un numero arbitriario de elementos
#Tenemos el ejemplo de los argumentos posicionales de la terminologia *args= Estos son los argumentos posicionales a una funcion
#Por lo que podemos recibirlos hasta una tupla de tipo de datos
#Tambien podemos recibir los tipo de argumentos de tipo **xwargs: Estos reciben en formate de diccionario de (clave,Valor)


print('--> Argumentos Variables <---')

# Aqui se implementas estas funcionaes quereciben con argumento "*args" estos se pasaran en formato de una tupla por lo que es importante
# Cabe destacar es el argumento args si o si debe ser el ultimo parametro, esta tupla
def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
superheroe_superpoderes('Ironam', 'Tony Stark', 'Armadura','Playboy','Millonario')

# Es opcional enviar argumentos variables, por lo que podemos declararlo en la funcion pero simplemente pasar del mismo cuando
# sea necesario en el mismo. Por lo que no nos generara ningun error en caso de que simplemente no lo utizemos.
superheroe_superpoderes('Mi vecino', 'Juan Perez')