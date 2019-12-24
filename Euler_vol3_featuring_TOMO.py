import math
import itertools

def vsota_stevk(n):
    '''Vrne vsoto stevk.'''
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota

def memo(fun):
    resitve = {}
    def mem_fun(x, y):
        if (x, y) not in resitve:
            resitve[x, y] = fun(x, y)
        return resitve[x, y]
    return mem_fun

def najlazja_pot_memo(A):
    @memo
    def rekurz_pomozna(i, j):
        polje = A[i][j]
        if i == j == 0:
            return polje
        elif i == 0:
            return rekurz_pomozna(i, j - 1) + polje
        elif j == 0:
            return rekurz_pomozna(i - 1, j) + polje
        else:
            return min(rekurz_pomozna(i - 1, j), rekurz_pomozna(i, j - 1)) + polje
    return rekurz_pomozna(len(A) - 1, len(A[0]) - 1)

def trikratna_pot_memo(A):
    '''se zacikla... :('''
    @memo
    def rekurz(i, j, dol=False, gor=False):
        polje = A[i][j]
        if j == 0:
            return polje
        elif i == 0:
            if gor:
                return rekurz(i, j - 1) + polje
            elif rekurz(i, j - 1) > rekurz(i + 1, j, dol=True):
                return min(rekurz(i, j - 1), rekurz(i + 1, j, dol=True)) + polje
            else:
                return min(rekurz(i, j - 1), rekurz(i + 1, j, dol=True)) + polje
        elif i == len(A) - 1:
            if dol:
                return rekurz(i, j - 1) + polje
            elif rekurz(i, j - 1) > rekurz(i - 1, j, gor=True):
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True)) + polje
            else:
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True)) + polje
        else:
            if gor:
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True)) + polje
            elif dol:
                return min(rekurz(i, j - 1), rekurz(i + 1, j, dol=True)) + polje
            elif min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True), rekurz(i + 1, j, dol=True)) == rekurz(i - 1, j, gor=True):
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True), rekurz(i + 1, j, dol=True))
            elif min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True), rekurz(i + 1, j, dol=True)) == rekurz(i + 1, j, dol=True):
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True), rekurz(i + 1, j, dol=True,))
            else:
                return min(rekurz(i, j - 1), rekurz(i - 1, j, gor=True), rekurz(i + 1, j, dol=True)) + polje
    skupaj = rekurz(len(A) - 1, 0)
    for konec in range(1, len(A[0])):
        skupaj = min(rekurz(len(A) - 1, konec), skupaj)
    return skupaj



def naloga81(k=1):
    '''Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.'''
    matrika = []
    with open('p081_matrix.txt', 'r') as dat:
        for vrstica in dat.readlines():
            line = vrstica.strip().split(',')
            matrika.append([int(a) for a in line])
    if k == 1:
        return najlazja_pot_memo(matrika)
    elif k == 2:
        return trikratna_pot_memo(matrika)


def verizni_ulomek_korena(n):
    if math.sqrt(n) % 1 == 0:
        return 0
    
    koren = round(math.sqrt(n), 1)
    a = int(koren)
    ulomek = [a]
    seznam = []
    game = []

    stevec = a
    im = n - stevec ** 2
    a = int((koren + stevec) / im)
    game.append((stevec, im))
    seznam.append(a)
    
    while True:
        stevec = -stevec + im * a
        im = (n - stevec ** 2) // im

        a = int((koren + stevec) / im)
        if (stevec, im) == game[0]:
            break
        game.append((stevec, im))
        seznam.append(a)
    ulomek.append(tuple(seznam))

    return len(seznam)

def naloga64(n):
    '''How many continued fractions for n ≤ 10000 have an odd period?'''
    st = 0
    for i in range(1, n + 1):
        if verizni_ulomek_korena(i) % 2 == 1:
            st += 1
    return st

def naloga65(k):
    '''Find the sum of digits in the numerator of the n-th convergent of the continued fraction for e.'''
    '''Resim s rekurzivno relacijo s predavanj ProseminarjaB.'''
    def a(i):
        if i % 3 == 2:
            return 2 * ((i // 3) + 1)
        else:
            return 1
    p_0 = 1
    p_1 = 2
    p = 2 + 1
    for i in range(2, k):
        p_0, p_1, p =  p_1, p, a(i) * p + p_1
    return vsota_stevk(p)

def verizni_ulomek_lih(m, n):
    a = int(m / n)
    ulomek = [a]
    seznam = []
    game = []

    stevec = n
    im = m - n * a
    while im != 0:
        a = int(stevec / im)
        game.append((stevec, im))
        seznam.append(a)
        stevec, im = im, stevec - im * a
    if len(seznam) % 2 == 0 and seznam != []:
        b = seznam[-1]
        del seznam[1]
        seznam.append(b - 1)
        seznam.append(1)
    ulomek.append(tuple(seznam))

    return ulomek

def naloga92(n):
    '''How many starting numbers below n will arrive at 89?'''
    # Rabi kakšno minutko
    def naslednji(k):
        nov = 0
        while k > 0:
            nov += (k % 10) ** 2
            k //= 10
        return nov
    vsi = 0
    for i in range(1, n + 1):
        while i != 1:
            if i == 89:
                vsi += 1
                break
            i = naslednji(i)
    return vsi


def naloga69(n):
    '''Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.'''
    #Poskusim memo, ker drugače traja in traja -- ŠE VEDNO TRAJA I guess, da par ur xD
    slovar = {}
    def prafaktorji(n):
        zac = n
        if n not in slovar:
            p = set()
            for a in range(2, n // 2 + 1):
                while n % a == 0:
                    p.add(a)
                    n //= a
                if n in slovar:
                    p.update(slovar[n])
                    break
            if len(p) == 0:
                slovar[zac] = [zac]
            else:
                slovar[zac] = list(p)
        return slovar[zac]

    def phi(n):
        resitev = n
        for p in prafaktorji(n):
            resitev *= (1 - (1 / p))
        return int(resitev)

    m = 1
    pravi = 1
    for a in range(2, n + 1):
        vrednost = a / phi(a)
        if vrednost >= m:
            m = vrednost
            pravi = a
    return pravi, m
        

#-----------------------------------------
def seznam_prastevil(n):
    sez = [2]
    a = 3
    while a < n:
        pr = True
        for k in sez:
            if a % k == 0:
                pr = False
                break
        if pr:
            sez.append(a)
        a += 1
    return sez

#5683
def naloga51(seznam):
    stevke = "0123456789"
    i = 5683
    seznam = seznam
    while i < len(seznam):
        stevilo = str(seznam[i])
        dolzina = len(stevilo)
        for koliko in [2,3,4]:
            for mesta in itertools.combinations([n for n in range(dolzina)], koliko):
                prastevil = 0
                switch = True
                a = stevilo[mesta[0]]
                for mesto in mesta:
                    if stevilo[mesto] != a:
                        switch = False
                        break
                if switch:
                    for x in stevke:
                        kopija = ""
                        for mesto in range(dolzina):
                            if mesto in mesta:
                                kopija += x
                            else:
                                kopija += stevilo[mesto]
                        if int(kopija) in seznam:
                            prastevil += 1
                if prastevil == 8:
                    return stevilo
        i += 1
                

def naloga99():
    #takes quite a while xD
    with open("p099_base_exp.txt", "r") as dat:
        najvecji = 1
        vrstica = 0
        for podatek in dat.readlines():
            baza, eks = podatek.strip().split(",")
            stevilo = int(baza) ** int(eks)
            if stevilo > najvecji:
                prava = vrstica
                najvecji = stevilo
            vrstica += 1
        return prava

                






