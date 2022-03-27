# Jakub Kroczek
# Ten algorytm sortowania w głównej mierze opiera się na sortowaniu Bubble-Sort i Merge-sort,
# dla k=1 zmodyfikowany Bubble-Sort, gdy są zamieniane dwa elementy to są już posortowane, więc wtedy następuje przeskok
# o dwa elementy, a gdy nie są zamieniane to o jedną pozycję
# dla 1<k<=log(n) w pierwszym przejściu liczę "n" i sortuję od razu Bubble sortem, a następnie jest Bubble-Sort,
# w którym główna pętla wykonuje się k-1 razy, bo +1 raz się wykonała przy wyliczaniu "n"
# dla k>log(n) jest to Merge-Sort
# Złożoność czasowa:
# k = Θ(1) => n
# k = Θ(log n) => n*log(n)
# k = Θ(n) => n*log(n)

from zad1testy import Node, runtests

def SortH(p, k):
    # tu prosze wpisac wlasna implementacje
    first = p
    if k == 1:
        pom = first
        pop = pom
        while pom.next != None:
            if pom.val > pom.next.val:
                tmp = pom.next
                pom.next = pom.next.next
                tmp.next = pom
                if tmp.next == first:
                    first = tmp
                    pop = tmp
                    continue
                pop.next = tmp
                pop = pop.next.next
                pom = pom.next
            else:
                pop = pom
                pom = pom.next
    else:
        n = 1
        pom = first
        pop = pom
        while pom.next != None:
            n += 1
            if pom.val > pom.next.val:
                tmp = pom.next
                pom.next = pom.next.next
                tmp.next = pom
                if tmp.next == first:
                    first = tmp
                    pop = tmp
                    continue
                pop.next = tmp
                pop = pop.next
            else:
                pop = pom
                pom = pom.next
        if n >= 2**k:
            for _ in range(k-1):
                pom = first
                pop = pom
                while pom.next != None:
                    if pom.val > pom.next.val:
                        tmp = pom.next
                        pom.next = pom.next.next
                        tmp.next = pom
                        if tmp.next == first:
                            first = tmp
                            pop = tmp
                            continue
                        pop.next = tmp
                        pop = pop.next
                    else:
                        pop = pom
                        pom = pom.next
        else:
            def scal_dwie_listy(a, b):
                if a.val <= b.val:
                    result = a
                    a = a.next
                else:
                    result = b
                    b = b.next
                pom = result
                while a != None and b != None:
                    if a.val <= b.val:
                        pom.next = a
                        a = a.next
                        pom = pom.next
                    else:
                        pom.next = b
                        b = b.next
                        pom = pom.next
                if a != None:
                    pom.next = a
                if b != None:
                    pom.next = b
                return result
            def stworz_sr(pocz):
                s = pocz
                w = pocz
                while (s.next != None and s.next.next != None):
                    s = s.next.next
                    w = w.next
                return w
            def merge_sort(t):
                if t == None or t.next == None:
                    return t
                sr = stworz_sr(t)
                sr_n = sr.next
                sr.next = None
                l = merge_sort(t)
                r = merge_sort(sr_n)
                posortowana = scal_dwie_listy(l, r)
                return posortowana
            first = merge_sort(first)
    return first
    pass


runtests( SortH ) 
