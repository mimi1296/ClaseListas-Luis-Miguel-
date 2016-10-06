n = int(input("Escriba el número de elementos de la lista: "))

def lista(n):
    Lista = []
    cont =0
    while cont<n:
        num = int(input("Numero {}: ".format(cont+1)))
        Lista.insert(cont,num)
        cont =cont + 1
        
    return Lista
def listaSinIndPar(lista):
    i= 0
    while (i < len(lista)):
        del lista[i]
        print("Eliminado el elemento ", lista[i], ", con indice ", i)
        i += 1
    return lista

lista = lista(n)
listasinpares = listaSinIndPar(lista)
print("La lista sin indices pares es: ", listasinpares)
