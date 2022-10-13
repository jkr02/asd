# Jakub Kroczek
# Sortuję tablicę S, tak abym miał największe skupiska śniegu po czym coraz mniejsze (Sortowanie: n*log(n))
# następnie znajduję taki indeks k (dzień) w którym już się nie będzie opłacało zbierać śniegu (liczba_śniegu-liczba_dni<=0),
# bo już go nie będzie, następnie dodaję wszystkie płaty śniegu i odejmując to co już stopniało
# Także nie ma znaczenia czy bedziemy zbierać śnieg od bramy wschodniej czy zachodniej czy w jakiejś tam kolejności
# interesuje nas tylko jakie płaty śniegu opłaca się zbierać do dnia gdzie juz nie bedzie śniegu
# Możemy zbierać po kolei płaty śniegu od bramy zachodniej jak występują w wąwozie i które znajdują się w posortowanej
# tablicy do indeksu "k" (bez indeksu "k") co gwarantuje nam, że zbierzemy tylko te płaty które są największe w dniu nr. 0
# zanim się roztopią
# złożoność czasowa: O(n*log(n)) - czas sortowania danych, reszta liniowo
# złożoność pamięciowa: O(1) - stała, chyba że sortowanie zabiera więcej pamięci
from egz1atesty import runtests

def snow( S ):
    n=len(S)
    S.sort(key=lambda x: -x)
    for i in range(n):
        if i>=S[i]:
            k=i
            break
        k=i
    suma=0
    for i in range(k):
        suma+=S[i]-i
    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
