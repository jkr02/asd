from random import randint
from time import time

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
def Bubble_sort(T):
    n=len(T)
    for y in range(n):
        for x in range(n-y-1):
            if T[x]>T[x+1]:
                T[x], T[x+1] = T[x+1], T[x]

def Insertion_sort(T):
    n=len(T)
    for x in range(1, n):
        temp = T[x]
        j=x-1
        while j>=0 and temp<T[j]:
            T[j+1] = T[j]
            j-=1
        T[j+1]=temp

def Merge_sort(T):
    n=len(T)
    if n>1:
        s=n//2
        l = T[:s]
        p = T[s:]
        Merge_sort(l)
        Merge_sort(p)
        d_l = len(l)
        d_p = len(p)
        i=j=k=0
        while i<d_l and j<d_p:
            if l[i] <= p[j]:
                T[k] = l[i]
                i+=1
            else:
                T[k] = p[j]
                j+=1
            k+=1
        while i<d_l:
            T[k]=l[i]
            i+=1
            k+=1
        while j<d_p:
            T[k]=p[j]
            j+=1
            k+=1
def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
def Counting_sort_mod(T):
    minimal = min(T)
    maximal = max(T)
    t=[[] for _ in range(maximal-minimal+1)]
    for x in range(len(T)):
        t[T[x]-minimal].append(T[x])
    k=0
    for x in range(len(t)):
        for y in range(len(t[x])):
            T[k] = t[x][y]
            k+=1

def Radix_sort(T):
    d = len(str(abs(max(T))))
    p = len(str(abs(min(T))))
    if p>d:
        d=p
    for x in range(d):
        t = [[] for _ in range(10)]
        m = [[] for _ in range(10)]
        for y in range(len(T)):
            if T[y]>=0:
                t[(T[y]//10**x)%10].append(T[y])
            else:
                m[(T[y] // 10 ** x) % 10].append(T[y])
        k = 0
        for i in range(len(m)):
            for y in range(len(m[i])):
                T[k] = m[i][y]
                k += 1
        for i in range(len(t)):
            for y in range(len(t[i])):
                T[k] = t[i][y]
                k += 1

def Selection_sort(T):
    n=len(T)
    for x in range(n-1):
        minimal = T[x]
        indeks=x
        for y in range(x+1, n):
            if T[y]<minimal:
                minimal=T[y]
                indeks = y
        T[x], T[indeks] = T[indeks], T[x]
def Partition(t, l, r):
    x=t[r]
    i=l-1
    for j in range(l, r):
        if t[j]<=x:
            i+=1
            t[i], t[j] = t[j], t[i]
    t[i+1], t[r] = t[r], t[i+1]
    return i+1
def Quick_sort(T):
    def quick_sort(t, l, r):
        while l<r:
            p = Partition(t, l, r)
            quick_sort(t, l, p-1)
            l=p+1
    quick_sort(T, 0, len(T)-1)

def Heap_sort(T):
    def heapify(tab, n, i):
        maksimum = i
        l=2*i
        p=2*i+1
        if l<n and tab[l]>tab[maksimum]:
            maksimum=l
        if p<n and tab[p]>tab[maksimum]:
            maksimum=p
        if maksimum!=i:
            tab[i], tab[maksimum] = tab[maksimum], tab[i]
            heapify(tab, n, maksimum)
    n=len(T)
    for i in range(n//2-1, -1, -1):
        heapify(T, n, i)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
def string_sort(T):
    n=len(T)
    d=len(T[0])
    for i in range(1, n):
        if len(T[i])>d:
            d=len(T[i])
    for i in range(d-1, -1, -1):
        tab = [[] for _ in range(27)]
        for j in range(n):
            if len(T[j]) > i:
                tab[ord(T[j][i])-96].append(T[j])
            else:
                tab[0].append(T[j])
        licznik = 0
        for j in range(27):
            for k in range(len(tab[j])):
                T[licznik] = tab[j][k]
                licznik+=1
    return T

def select(T, p, k, r):
    if p==r:
        return T[p]
    if p<r:
        q=Partition(T, p, r)
        if q==k:
            return T[q]
        elif q<k:
            return select(T, q+1, k, r)
        else:
            return select(T, p, k, q-1)

# tab = [randint(0, 10**4) for _ in range(10501)]
# tab1=tab.copy()
# start=time()
# tab.sort()
# stop=time()
#print(tab)
# print(stop-start, "s", sep="")
#############################
def partit(A, p, r):
    x=A[r]
    i=p-1
    for j in range(p, r):
        if A[j]<=x:
            i+=1
            A[i], A[j]=A[j],A[i]
    A[i+1], A[r]=A[r], A[i+1]
    return i+1
def sel(A, p, k, r):
    if p==r:
        return A[p]
    if p<r:
        q=partit(A, p, r)
        if q==k: return A[q]
        elif q<k: return sel(A, q+1, k, r)
        else: return sel(A, p, k, q-1)
t=[5, 2, 1, 4, 2, 3, 7]
Merge_sort(t)
print(t)