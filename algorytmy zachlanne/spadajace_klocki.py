T = [[1, 5], [3, 4], [4, 5], [3, 5], [4, 5], [2, 3], [1, 2]]
def spadajace_klocki(T):
    T.sort(key=lambda x: (x[1], -x[0]))
    licznik=0
    r=T[0][1]
    for x in range(1, len(T)):
        if T[x][0]<r:
            licznik+=1
        else:
            r=T[x][1]
    return licznik
print(spadajace_klocki(T))