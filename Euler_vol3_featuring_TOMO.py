import math


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
                return rekurt(i, j - 1) + polje
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
