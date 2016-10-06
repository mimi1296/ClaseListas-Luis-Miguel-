# Control de versiones
# GitHub


def Mayor(rango):
    Lista = []
    c = 0
    while c < rango:
        num = eval(input("Numero {} ".format(c+1)))
        Lista.insert(c,num)
        c = c+1
    mayor = max(Lista)
    return mayor

rango = int(input("Ingrese el rango de la lista, por favor: "))
mayor = Mayor(rango)
print("El número mayor es:", mayor)
    
