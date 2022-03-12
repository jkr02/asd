# Jakub Kroczek
# Ten algorytm sortowania w głównej mierze opiera się na sortowaniu Bubble-Sort, wiedząc że lista jest k-chaotyczna
# można wydedukować, że przejdzimy po tablicy k razy, gdyż w jednej iteracji dany element zmienia położenie o conajmniej
# jedną pozycję w kierunku miejsca, gdzie będzie się znajdowało na posortowanej pozycji.
# Złożoność czasowa:
# k = Θ(1) => n
# k = Θ(log n) => n*log(n)
# k = Θ(n) => n**2

from zad1testy import Node, runtests


def SortH(p, k):
    # tu prosze wpisac wlasna implementacje
    # BUBBLE SORT
    first = p
    # dla k=1, jak zamienimy pozycjami dwa elementy to są one już posortowane, więc możemy wziąć następne dwa elementy
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
        for _ in range(k):
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
    # def sortedMerge(a, b):
    #     if a.val <= b.val:
    #         result = a
    #         a = a.next
    #     else:
    #         result = b
    #         b = b.next
    #     pom = result
    #     while a != None and b != None:
    #         if a.val <= b.val:
    #             pom.next = a
    #             a = a.next
    #             pom = pom.next
    #         else:
    #             pom.next = b
    #             b = b.next
    #             pom = pom.next
    #     if a != None:
    #         pom.next = a
    #     if b != None:
    #         pom.next = b
    #     return result
    # def getMiddle(head):
    #     if (head == None):
    #         return head
    #     slow = head
    #     fast = head
    #
    #     while (fast.next != None and
    #            fast.next.next != None):
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #     return slow
    # def merge_sort(l):
    #     if l == None or l.next == None:
    #         return l
    #     sr = getMiddle(l)
    #     sr_n = sr.next
    #     sr.next = None
    #     left = merge_sort(l)
    #     right = merge_sort(sr_n)
    #     sorted_list = sortedMerge(left, right)
    #     return sorted_list
    # first = merge_sort(first)
    return first
    pass


runtests( SortH ) 
