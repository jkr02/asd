def czy_da_sie(T, a, b):
    T.sort(key=lambda x: (T[x][0], T[x][1]))
    tab=[0 for _ in range(b-a+2)]
    tab[0]=1
    for i in range(len(T)):
        if T[i][0]>=a and T[i][1]<=b:
            if tab[T[i][0]-a]==1 and tab[T[i][1]-a]==0:
                tab[T[i][1]-a]=1
                if tab[-1]==1:
                    return True
    return False
def zadanie_jak_wyzej(T, a, b):
    # O(nlog(n) + (b-a))
    T.sort(key=lambda x: (T[x][0], T[x][1]))
    tab = [0 for _ in range(b - a + 2)]
    tab[0]=1
    for i in range(len(T)):
        if T[i][0] >= a and T[i][1] <= b:
            if tab[T[i][0]-a] >= 1 and (tab[T[i][1]-a]==0 or tab[T[i][0]-a]+T[i][2] < tab[T[i][1]-a]):
                tab[T[i][1]-a] = tab[T[i][0]-a]+T[i][2]
    return tab[-1]-1
