def det(matrika):
    if len(matrika) == 1:
        return int(matrika[0][0])
    n = len(matrika)
    if n > 2:
        kofaktor = 1
        stolpec = 0
        vsota = 0
        while stolpec <= n-1:
            slovar = {}
            vrstica = 1
            while vrstica <= n-1:
                m = 0 #števec stolpcev
                slovar[vrstica] = []
                while m <= n-1:
                    if m != stolpec: #doda element v slovar podmatrike, če ni v m-tem stolpcu
                        slovar[vrstica].append(matrika[vrstica][m]) 
                    m += 1
                vrstica += 1
            podmatrika = [slovar[x] for x in slovar]
            vsota = vsota + kofaktor * (matrika[0][stolpec]) * (det(podmatrika))
            kofaktor = kofaktor * (-1)
            stolpec += 1
        return vsota
    else:
        return (matrika[0][0]* matrika[1][1] - matrika[0][1] * matrika[1][0])

def transponiraj(matrika):
    m = len(matrika)
    n = len(matrika[0])
    transponirana = []
    for i in range(n):
        vrstica = []
        for j in range(m):
            vrstica.append(matrika[j][i])
        transponirana.append(vrstica)
    return transponirana

import copy
def inverzna(matrika):
    determinanta = det(matrika)
    if determinanta == 0:
        print("Singularna matrika - inverzna matrika ne obstaja.")
        return
    else:
        dimenzija = len(matrika)
        invmat = [[0 for x in range(dimenzija)] for x in range(dimenzija)]
        for v in range(0, dimenzija):
            for s in range(0, dimenzija):
                podmatrika = copy.deepcopy(matrika)
                podmatrika.pop(v)
                for seznam in podmatrika:
                    seznam.pop(s)
                invmat[s][v] = det(podmatrika) #ker potrebujemo transponirano adjungiranko
        for v in range(0, dimenzija):
            for s in range(0, dimenzija):
                invmat[s][v] /= determinanta
                if (v + s) % 2 != 0:
                    invmat[s][v] *= -1
        return invmat

print(inverzna([[1,2,3],[4,5,6],[7,8,9]]))
    
mat = [[1,2,3],[4,5,6],[7,2,9]]
print(inverzna(mat))

print("AAAAAA")

mat2 = [[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]
print(inverzna(mat2))
    
