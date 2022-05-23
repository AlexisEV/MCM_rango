import math

#Función para detectar un error al momento de ingresar los límites del rango

def error(inf,sup):

    #El número inferior no puede ser igual o menor a 0

    if inf <= 0:
        print("Por favor ingrese un límite inferior mayor a 0")
        return True

    #El número superior no puede ser menor que el inferior

    elif sup < inf:
        print("El límite superior debe ser mayor al inferior")
        return True
    else:
        return False

#Función para crear el rango de números

def crear_rango():

    while True:

        #Try-except para controlar errores al ingresar datos no numéricos.
        try:
            NUMERO_INFERIOR = int(input("Ingrese límite inferior mayor a 0: "))
            NUMERO_SUPERIOR = int(input("Ingrese límite superior: "))

        except ValueError:
            print("Por favor ingrese números naturales")
            continue

        #Si no hay algún otro error, se rompe el bucle
        if not error(NUMERO_INFERIOR,NUMERO_SUPERIOR):
            break

    rango = list(range(NUMERO_INFERIOR,NUMERO_SUPERIOR + 1))

    return rango

#Función para detectar si un número es primo

def es_primo(num):

    for i in range(2,num):
        #Los números primos solo son divisibles por si mismos y por el 1
        if num%i == 0:
            return False
    return True

#Función para listar todos los números primos desde el 2 hasta el límite superior del rango

def listar_primos(rango):

    lista_primos = []
    for i in range(2,rango[-1]+1):
        #Si el num es primo, se almacena en la lista
        if es_primo(i):
            lista_primos.append(i)
    return lista_primos
    
#Función para calcular el MCM de un rango de números mayores a 0 

def mcm():

    rango = crear_rango()
    lista_primos = listar_primos(rango)
    sup = rango[-1]
    inf = rango[0]
    indice = 0              #Indice para seleccionar a los números primos del listado
    lista_fact_primos = []  #Lista que almacena los factores primos del rango de números

    #Bucle que se ejecutará hasta que todos los elementos del rango sean 1

    while {1}  != set(rango):
        
        #División de todos los números del rango

        rango2 = list(map(lambda x: x/lista_primos[indice] if x%lista_primos[indice] == 0 else x, rango)) 

        #Si la nueva lista es igual a la original, se pasa al siguiente primo de la lista

        if rango2 == rango:
            indice += 1 
            continue

        #Si la nueva lista y la original no son iguales, se agrega el num primo a la lista de factores primos

        lista_fact_primos.append(lista_primos[indice])

        rango = rango2

    MCM = math.prod(lista_fact_primos)

    print("El MCM de los números desde el {0} hasta el {1} es {2}".format(inf,sup,MCM))


mcm()
