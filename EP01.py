import time
import timeit
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
    return quicksort(menores) + iguais + quicksort(maiores)

def insercao(lista):
    for j in range(1,len(lista)):
        c = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > c:
            lista[i + 1] = lista[i]
            i -= 1
        v[i + 1] = c

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
    x=1
    lista=[]
    tabela =(
        "|------------------------[EP1 - Vale a pena ordenar?]------------------------- |\n"
        "|  Aluno(s): FELIPE GOMES - FATEC - SJC                                        |\n"
        "|  Estrutura de Dados - ADS                                                    |\n"
        "|  Algoritmo(s) escolhido(s): todos                                            |\n"
        "|             Tempos de Ordenacao                   Numero de Buscas           |\n"          
        "|------------------------------------------------------------------------------|\n"
        "|   n   | Insercao  Selecao  Merge. Quick. | Insercao  Selecao  Merge.  Quick. |\n"
        "|-------|----------------------------------------------------------------------|\n")
    while x <= ciclo:

        for i in range(n):
            i=random.randrange(1, 2000, 1)
            lista.append(i)

        ini1 = time.time()
        mergesort(lista)
        fim1 = time.time()
        merge=fim1-ini1
    
        ini2 = time.time()
        quicksort(lista)
        fim2 = time.time()
        quick=fim2-ini2
        
        ini3=time.time()
        selecao(lista)
        fim3=time.time()
        selec=fim3-ini3
        
        print(n)
        print ("Função mergesort: ", merge)
        print ("Função quicksort: ", quick)
        print ("Função selecao: ", selec)
        x+=1
        n+=2000
