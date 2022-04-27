#zaba skacze na pola z jedzeniem. obliczyc najmniejsza liczbe skokow do pola n-1
#f(i, y)=najmniejsza liczba ruchow na dane pole z najwieksza liczba energii
#f(0,price)

tab=[4, 5, 0, 0, 2, 3, 0, 0, 0]
n=len(tab)
if tab[0]>=n-1:
    pass
t=[[[0, 0] for _ in range(n)] for _ in range(n)]
t[0][0][1]=tab[0]
for i in range(n):
    t[i][0][1]=1
for i in range(1, n-1):
    for y in range(n):
