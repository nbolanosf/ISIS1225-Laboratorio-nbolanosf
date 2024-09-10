# FUNCIÓN 2 - O()

def contar_ocurrencias(my_lst, x):
    """
    Contar el numero de ocurrencias de x al interior de my_lst
    param my_lst: linked list con los numeros
    type my_lst: dict (representa una linked list)
    param x: elemento a contar ocurrencias en la lista
    Return: numero de ocurrencias de x en my_lst
    """
    conteo = 0
    actual= my_lst['first']

    while actual != None:
        if actual['info'] == x:
            conteo += 1
        actual = actual['next']
    
    return conteo


# [20, 14, 6, 28, 10, 14, 62, 10, 14]

print(contar_ocurrencias({'first': {'info': 20, 'next': {'info': 14, 'next': {'info': 6, 'next': {'info': 28, 'next': {'info': 10, 'next': {'info': 14, 'next': {'info': 62, 'next': {'info': 10, 'next': {'info': 14, 'next': None}}}}}}}}}}, 50))