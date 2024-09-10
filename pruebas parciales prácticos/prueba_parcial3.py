def contar_ocurrencias_al(my_lst, x): 
    """
    Contar el numero de ocurrencias de x al interior de my_lst
    param my_lst: array list con los numeros
    type my_lst: dict (representa un array list)
    param x: elemento a contar ocurrencias en la lista
    Return: numero de ocurrencias de x en my_lst
    """
    conteo = 0

    for elem in my_lst['elements']:
        if elem == x:
            conteo += 1
    
    return conteo

def contar_ocurrencias_sll(my_lst, x):
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

def buscar_mas_repetido(my_lst, tipo='Single_Linked_List'):
    """
    Buscar el numero que se repite mas veces en la lista my_lst
    param my_lst: list con los numeros
    type my_lst: dict (representa una list)
    Return: numero que se repite más veces en la lista my_lst
    """
    ocurrenc = []
    revisados = []

    if tipo == 'Array_List':
        for elem in my_lst['elements']:
            if elem not in revisados:
                revisados.append(elem)
                temp = (elem, contar_ocurrencias_al(my_lst, elem))
                ocurrenc.append(temp)
    else:
        actual = my_lst['first']
        while actual != None:
            if actual['info'] not in revisados:
                revisados.append(actual['info'])
                temp= (actual['info'], contar_ocurrencias_sll(my_lst, actual['info']))
                ocurrenc.append(temp)
            actual = actual['next']
    
    max_num = None
    max_rep = 0

    for elem in ocurrenc:
        if elem[1] >= max_rep:
            max_rep = elem[1]
            if not max_num:
                max_num = elem[0]
            elif elem[0] > max_num:
                max_num = elem[0]
    
    return max_num


print(buscar_mas_repetido({'first': {'info': 10, 'next': {'info': 14, 'next': {'info': 6, 'next': {'info': 28, 'next': {'info': 10, 'next': {'info': 14, 'next': {'info': 6, 'next': {'info': 10, 'next': {'info': 14, 'next': None}}}}}}}}}}))
                

    