# sa drzewa, które maja wartosc i musi byc odstep pomiedzy scietym drzewem
# f(i) - najwiekszy zysk, gdy wezmiemy i-te drzewo
# g(i) - najwiekszy zysk, gdy nie wezmiemy i-tego drzewa
# f(0)=0
# g(0)=0
# g(i)=max(f(i-1), g(i-1))
# f(i)=g(i-1)+T(i)
tab = [3, 1, 5, 7, 2]
def drzewa(T):
    n=len(T)
    tab = [0 for _ in range(2*n)]
    for i in range(n):
        tab[2*i] = max(tab[2*i-1], tab[2*i-2])
        tab[2*i+1] = tab[2*i-2] + T[i]
    return tab[2*n-1]
print(drzewa(tab))