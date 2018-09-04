#matrika1 = [[1,2,3],[4,5,6],[7,8,9]]
def pretvorba_niza_v_seznam(ss):
    seznam = []
    ss = ss[1:len(ss)- 1]
    for i in range (0, len(ss)):
        if ss[i] == '[':
            vrstica = []
        elif ss[i] != '[' and ss[i] != ']':
            vrstica += [ss[i]]
        else:
            seznam += [vrstica]
    novseznam = []
    for vrstica in seznam:
        novavrstica = []
        for element in vrstica:
            if element != ',':
                novavrstica += [float(element)]
        novseznam += [novavrstica]
    return novseznam

def transponiraj(mat):
    m = len(mat)
    n = len(mat[0])
    transponirana = []
    for i in range(n):
        vrstica = []
        for j in range(m):
            vrstica.append(mat[j][i])
        transponirana.append(vrstica)
    return transponirana

def det(matrika):
    n = len(matrika)
    if (n>2):
        kofaktor = 1
        stolpec = 0
        vsota = 0
        while stolpec <= n-1:
            d={}
            t1=1
            while t1 <= n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if m != stolpec:
                        d[t1].append(matrika[t1][m])
                    m+=1
                t1+=1
            podmatrika =[d[x] for x in d]
            vsota = vsota + kofaktor*(matrika[0][stolpec])*(det(podmatrika))
            kofaktor = kofaktor * (-1)
            stolpec += 1
        return vsota
    else:
        return (matrika[0][0]*matrika[1][1]-matrika[0][1]*matrika[1][0])

import copy
def inverzna(matrika):
    determinanta = det(matrika)
    if det == 0:
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



#Program matricnik
def meni():
    print (" M A T R I Č N I K, program za računanje z matrikami")
    print (30 * '-')
    print ("1. Transponiranje")
    print ("2. Determinanta")
    print ("3. Izhod")
    print (30 * '-')

## INPUT ###
    izbira = input('Izberi operacijo [1-3] : ')

    if izbira == '1':
        print ("Vnesi matriko (seznam seznamov)")
        matrika = input()
        tmp = pretvorba_niza_v_seznam(matrika)
        print("Transponirana matrika: " , transponiraj(tmp))
        meni()
    elif izbira == '2':
        print ("Vnesi kvadratno matriko (seznam seznamov)")
        matrika = input()
        tmp = pretvorba_niza_v_seznam(matrika)
        print("Determinanta je " , det(tmp))
        meni()
    elif izbira == '3':
        print ("Hvala za sodelovanje")
        exit 
    else:
        print ("Vaša izbira ne obstaja")
        meni()
 
meni()
