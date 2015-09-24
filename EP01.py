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
    ini2 = time.time()
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    if len(lista) <= 1:
        return lista
    #tudo = quicksort(menores) + iguais + quicksort(maiores)
    lista=[menores+iguais+maiores]
    fim2 = time.time()
    quick=fim2-ini2
    return quick

def insercao(lista):
    ini4=time.time()
    for j in range(1,len(lista)):
        c = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > c:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = c
    fim4=time.time()
    inser=fim4-ini4
    return inser

def selecao(lista):
    ini3=time.time()
    n = len(lista)
    for i in range(n-1):
        x = i
        for j in range(i+1,n):
          if lista[j] < lista[x]:
              x = j
              lista[i],lista[x] = lista[x],lista[i]
    fim3=time.time()
    selec=fim3-ini3
    return selec

def main():
    n=2000
    ciclo=2
    x=0
    lista=[]

    while x <= ciclo:
        print(n)
        for i in range(n):
            i=random.randrange(20000)
            lista.append(i)
            lista.sort()

        ini1 = time.time()
        mergesort(lista)
        fim1 = time.time()
        merge=fim1-ini1
        
        print ("Função insercao:  ", insercao(lista))
        print ("Função mergesort: ", merge)
        print ("Função quicksort: ", quicksort(lista))
        print ("Função selecao:   ", selecao(lista))
        x,n = x+1, n+2000        


    tabela =(
        "|------------------------[EP1 - Vale a pena ordenar?]------------------------- |\n"
        "|  Aluno(s): FELIPE GOMES - FATEC - SJC                                        |\n"
        "|  Estrutura de Dados - ADS                                                    |\n"
        "|  Algoritmo(s) escolhido(s): todos                                            |\n"
        "|             Tempos de Ordenacao                   Numero de Buscas           |\n"          
        "|------------------------------------------------------------------------------|\n"
        "|   n   | Insercao  Selecao  Merge. Quick. | Insercao  Selecao  Merge.  Quick. |\n"
        "|-------|----------------------------------------------------------------------|\n")
