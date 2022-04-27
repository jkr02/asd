import queue
tab = [3, 5, 7, 2, 3, 1]
P = queue.PriorityQueue()
for x in range(len(tab)):
    P.put((tab[x], x))
for x in range(len(tab)):
    a, b = P.get()
    print(a, b)