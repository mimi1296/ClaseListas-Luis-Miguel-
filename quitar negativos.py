def quitarNegativos(a):
    cont =0
    print("Lista original: ",a)
    while cont<len(a):
        if a[cont] < 0:
            a[cont] = 0
        else:
            a[cont] =a[cont]
        cont =cont +1
    print("Lista sin negativos: ", a)

quitarNegativos([3, -2, -1, -10, 4, -5])
