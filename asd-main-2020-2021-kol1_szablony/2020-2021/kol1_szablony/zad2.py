from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None     
    self.next = None 



def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    w = Node()
    w.next = p
    for _ in range(k):
        pop = w.next
        temp = pop.next
        if pop.val > temp.val:
            w.next, pop.next, temp.next = temp, temp.next, pop
            temp, pop = pop, temp
        while temp.next:
            if temp.val>temp.next.val:
                pop.next, temp.next.next, temp.next = temp.next, temp, temp.next.next
            pop = pop.next
            temp = pop.next
    return w.next

    pass


runtests( SortH ) 