def section(T, p, q):
    pom=0
    minimum=min(T)
    maksimum=max(T)
    def kubelkowe(t):
        tab=[[]for _ in range((int(maksimum-minimum))+1)]
        for i in range(len(T)):
            tab[int(T[i]-minimum)].append(T[i])
        return tab
    tab = kubelkowe(T)
    for i in range(len(tab)):
        pom+=len(tab[i])
        if pom > p:
            l=i
            left=pom
            for j in range(len(tab[i])):
                pass
        if pom >= q:
            r=i
            break