#Repaso con funcion Suma ene esta caso aplicamos la idea de Modulo
import Modulo_Funcion_Sumar

#Tenemos dos formas de importar

#import Modulo_Funcion_Sumar 1ra Forma de importar
from Modulo_Funcion_Sumar import sumar #Segunda forma de importacion

print('--> Función sumar <--')

# Llamar a la funcion
#resultado_funcion = Modulo_Funcion_Sumar.sumar(8, 5) Esta forma corresponderia a la primera forma para su uso.
resultado_funcion = sumar(8, 5) #Ahora se puede usar de la misma manera de siempre. con la segunda forma.

print(f'Resultado función sumar: {resultado_funcion}')

resultado_funcion = sumar(9, 15)
print(f'Resultado función sumar: {resultado_funcion}')

