from queue import PriorityQueue
from zad2testy import runtests


def robot( L, A, B ):
    tab=[[[[-1, -1, -1] for _ in range(4)] for _ in range(len(L[0]))] for _ in range(len(L))]
    vector=[(1, 0), (0, -1), (-1, 0), (0, 1)]
    t=[60, 40, 30]
    q=PriorityQueue()
    q.put((0, A[0], A[1], 0, 0))
    while not q.empty():
        time, x, y, kierunek, distance = q.get()
        if (x, y) == B:
            return time
        if tab[y][x][kierunek][distance]!=-1 or L[y][x]=='X':
            continue
        q.put((time + 45, x, y, (kierunek+1)%4, 0))
        q.put((time + 45, x, y, (kierunek+3)%4, 0))
        tab[y][x][kierunek][distance]=time
        q.put((time+t[distance], x+vector[kierunek][0], y+vector[kierunek][1], kierunek, min(distance+1, 2)))
    return None
    
runtests( robot )


