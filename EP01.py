import time
import random

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    #tudo = quicksort(menores) + iguais + quicksort(maiores)
    return menores+iguais+maiores

def insercao(lista):
    for j in range(1,len(lista)):
        c = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > c:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = c

def selecao(lista):
  n = len(lista)
  for i in range(n-1):
    x = i
    for j in range(i+1,n):
      if lista[j] < lista[x]: x = j
      lista[i],lista[x] = lista[x],lista[i]


def main():
    n=2000
    ciclo=2
    x=0
    lista=[]

    while x <= ciclo:
        for i in range(n):
            i=random.randrange(1, 2000, 1)
            lista.append(i)
        exec1(lista)
        x,n = x+1, n+2000
        print(n)
        

def exec1(lista):
    ini3=time.time()
    selecao(lista)
    fim3=time.time()
    selec=fim3-ini3

    ini4=time.time()
    insercao(lista)
    fim4=time.time()
    inser=fim4-ini4
    
    ini1 = time.time()
    mergesort(lista)
    fim1 = time.time()
    merge=fim1-ini1
    
    ini2 = time.time()
    quicksort(lista)
    fim2 = time.time()
    quick=fim2-ini2
        
    print ("Função insercao:  ", inser)
    print ("Função mergesort: ", merge)
    print ("Função quicksort: ", quick)
    print ("Função selecao:  ", selec)
