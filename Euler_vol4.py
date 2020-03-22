from functools import lru_cache

def problem62(k):
    '''Find the smallest cube for which exactly k permutations of its digits are cube.'''
    slovar = {}


    def v_seznam(st):
        s = "0" * 10
        for a in str(st):
            a = int(a)
            stevka = int(s[a]) + 1
            s = s[:a] + str(stevka) + s[a+1:]
        if s not in slovar:
            slovar[s] = [st, 1]
        else:
            if slovar[s][1] == k-1:
                return slovar[s][0]
            slovar[s][1] += 1
    
    i = 10
    while True:
        resitev = v_seznam(i*i*i)
        if resitev is not None:
            return resitev
        i += 1 
    
def pet_kotno(n):
    return (n * (3*n - 1) // 2 , n * (3*n + 1) // 2 )

def naloga78(e):

    # stevilo razdelitev stevila n, na neničelne člene
    # formula iz predavanj diskretne matematike
    @lru_cache(maxsize=None)
    def p(n):
        if n == 0:
            return 1

        vrednost = 0

        i = 1
        while True:
            prvo, drugo = pet_kotno(i)
            if n >= prvo:
                vrednost += ((-1) ** (i+1)) * p(n - prvo)
            else:
                break
            if n >= drugo:
                vrednost += ((-1) ** (i+1)) * p(n - drugo)
            
            i += 1
        
        return vrednost
    
    a = 1
    while True:
        if (p(a) % 10**e == 0):
            return (a, p(a))
        a += 1

