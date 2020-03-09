def to_binary(n):
    binarno = ""
    n = int(n)
    while len(binarno) < 7:
        binarno = str(n % 2) + binarno
        n //= 2
    return binarno

def from_binary(n):
    prava = 0
    for i in range(7):
        if n[-i-1] == "1":
            prava += 2 ** i
    return prava


def xor(a, b):
    nov = ""
    for i in range(7):
        if a[i] == b[i]:
            nov += "0"
        else:
            nov += "1"
    return nov

def naloga59(dat):
    with open(dat, "r") as f:
        znaki = f.read().split(",")
    # 32 - 90 and 97 - 122 is ok
    # key from 97 - 122

    for i in range(97, 123):
        for j in range(97, 123):
            for k in range(97, 123):
                key = [str(i), str(j), str(k)]
                i = 0
    
                zapis = ""

                for znak in znaki:
                    d = from_binary(xor(to_binary(znak), to_binary(key[i])))
                    if 32 <= d <= 90 or 97 <= d <= 122:
                        zapis += chr(from_binary(xor(to_binary(znak), to_binary(key[i]))))
                        i += 1
                        if i == 3:
                            i -= 3
                    else:
                        napaka = True
                        break
                if not napaka:
                    return zapis
    

print(naloga59("p059_cipher.txt"))