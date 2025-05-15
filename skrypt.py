ne1=[1, 2, 2, 3, 3, 3, 4]  # zwraca: 3
ne2=["a", "b", "a", "c", "a"]


def ne(lista):
    licznik={}
    for i in lista:
        if i in licznik:
            licznik[i] += 1
        else:
            licznik[i] = 1
    
    return max(licznik.values())

print (ne(ne1))
print (ne(ne2))
