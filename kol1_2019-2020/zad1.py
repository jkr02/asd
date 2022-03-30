#złożoność czasowa:  O(nlog(n) + d*n)
#złożoność pamięciowa:  O(n)

def pretty_sort(T):
    def liczba_liczb(a):
        b = a
        if b==0:
            return 1, 0
        cyfry = [0 for _ in range(10)]
        while b!=0:
            cyfry[b%10]+=1
            b//=10
        j = 0
        m = 0
        for i in range(10):
            if cyfry[i]==1:
                j+=1
            elif cyfry[i]>1:
                m+=1
        return j, m

    def merge_sort(t):
        k=len(t)
        if k>1:
            #a=T[index:index+k]
            mid = k//2
            l=t[:mid]
            p=t[mid:]
            merge_sort(l)
            merge_sort(p)
            i=j=r=0
            while i<len(l) and j<len(p):
                if l[i][0] < p[j][0]:
                    t[r] = l[i]
                    #T[index+r] = a[i]
                    r+=1
                    i+=1
                elif p[j][0] < l[i][0]:
                    t[r] = p[j]
                    #T[index+r] = a[mid+j]
                    r+=1
                    j+=1
                else:
                    if l[i][1]<=p[j][1]:
                        t[r] = l[i]
                        #T[index + r] = a[i]
                        r += 1
                        i += 1
                    else:
                        t[r] = p[j]
                        #T[index + r] = a[mid + j]
                        r += 1
                        j += 1
            while i<len(l):
                t[r] = l[i]
                #T[index+r] = a[i]
                r+=1
                i+=1
            while j<len(p):
                t[r] = p[j]
                #T[index+r] = a[mid+j]
                r+=1
                j+=1

    n=len(T)
    tab = [[0, 0, 0]for _ in range(n)]
    for i in range(n):
        tab[i][0], tab[i][1] = liczba_liczb(T[i])
        tab[i][2] = T[i]
    merge_sort(tab)
    for i in range(n):
        T[i] = tab[i][2]
abc = [111234, 1234, 11234, 1, 45, 123546, 2345444312]
pretty_sort(abc)
print(abc)