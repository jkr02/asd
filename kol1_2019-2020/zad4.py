import time


def tanagram(x, y, t):
    n=len(x)
    tab_x=[[]for _ in range(26)]
    tab_y=[[]for _ in range(26)]
    for i in range(n):
        tab_x[ord(x[i])-97].append(i)
        tab_y[ord(y[i])-97].append(i)
    for i in range(26):
        for j in range(len(tab_x[i])):
            if t<abs(tab_x[i][j]-tab_y[i][j]):
                return False
    return True




x ="kotomysz"
y="tokmysoz"
t=3
start=time.time()
print(tanagram(x, y, t))
stop=time.time()
print(stop-start)