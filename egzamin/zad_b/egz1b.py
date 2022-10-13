# Jakub Kroczek
# zamysł jest taki, żeby każdemu wierzchołkowi dać trzy tablice, i do każdej wpisywać kolejno: odległości od wierzchołków ojca,
# następnie odległości od wierzchołków które są jego lewymi synami, i następnie do trzeciej odległości od wierzchołków, które są
# jego prawymi synami w miarę wchodzenia w dół dla każdego wierzchołka przypisujemy do pierwszej tablicy odległości
# od ojca-ojca, i ojca-prawego, bądź ojca-lewego syna itd.
# następnie dla każdego wierzchołka sprawdzić jaka jest najczęstsza odległość od wierzchołków,
# wraz z stopniem głębokości i wybrać ten co ma największy i sprawdzić ile minimalnie krawędzi można usunąć, jeśli jest
# wiele takich wierzchołków co mają taką samą największą liczbę liści (po usunięciu krawędzi) i tą samą głębokość,
# to trzeba wybrać ten w którym jest możliwe usunięcie najmniejszej liczby krawędzi
# złożoność czasowa: n^2
from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow
def wideentall( T ):
    T.x=0
    maks=0
    n=0
    tab=[[]]
    def liczba_wierzcholkow(T):
        nonlocal n, maks, tab
        if maks<T.x:
            maks=T.x
            tab.append([T])
        else:
            tab[T.x].append(T)
        if T.left!=None:
            T.left.x=T.x+1
            liczba_wierzcholkow(T.left)
        if T.right!=None:
            T.right.x = T.x + 1
            liczba_wierzcholkow(T.right)
        n+=1
    liczba_wierzcholkow(T)
    t=[[[]],[[]],[[]]]*n
    depth=0
    def wyszukaj(T, d):
        if T.left!=None:
            pass

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )