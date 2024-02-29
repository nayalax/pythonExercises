# How to use Tuples
# Crea una tupla e intenta modificar su contenido
myTuple = (1,2,3)
try:
    myTuple[1] = 5
except Exception as e:
    print(e)

# Creamos una tupla mixta. Recuerda que una tupla es inmutable y puede contener otro tipos de datos como listas, cadenas, enteros, etc.  
mixed_tuple=(1,"two",[3,4],{5:"five"},(6,7),8.0,True,None,{9})

# Pregunta podríamos modificar el contenido del tercer elemento tupla_mixta[2]? Escribe el código necesario e inténtalo. 
# Luego imprime la tupla y observa si ha funcionado o no.
mixed_tuple[2][1] = 3
print(mixed_tuple)

# Imprime los elementos de la tupla con un loop for y su tipo
# Ejemplo 1 => <class'int'>
# dos => <class'str'>
# Para concatenar el valor del elemento con su tipo tendremos que hacer casting de ambos con str() o usar un fstring
for x in mixed_tuple:
    print(type(x))