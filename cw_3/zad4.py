def scal(a, b):
    i_a=0
    i_b=0
    d_a = len(a)
    d_b=len(b)
    tab = [0 for _ in range(d_a+d_b)]
    i_t=0
    while i_a < d_a and i_b<d_b:
        if a[i_a] <= b[i_b]:
            tab[i_t] = a[i_a]
            i_a+=1
        else:
            tab[i_t] = b[i_b]
            i_b += 1
        i_t+=1
    while i_a<d_a:
        tab[i_t] = a[i_a]
        i_a+=1
        i_t+=1
    while i_b < d_b:
        tab[i_t] = b[i_b]
    return tab


def scalanie(tab, k):
    for x in range(0, k + 1, 2):
        scal(tab[x], tab[x+1])

    scalanie(tab, k//2)