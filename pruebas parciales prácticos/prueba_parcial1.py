# FUNCIÓN 1 - O(N)

def contar_ocurrencias(my_lst, x): 
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

num = int(input('Ingrese un número: '))
answer = contar_ocurrencias({'elements': [20, 14, 6, 28, 10, 14, 62, 10, 14]}, num)
print(answer)