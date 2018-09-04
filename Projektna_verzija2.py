#input je vedno string (niz), zato za začetni program kmečka funkija, ki pretvori takšen input v seznam
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
#---------------------------FUNKCIJE---------------------------
def det(matrika):
    st_vrstic = len(matrika)
    st_stolpcev = len(matrika[0])
    if st_vrstic != st_stolpcev:
        print("Determinante lahko izračunamo samo kvadratnim matrikam")#Ko je input grafično urejen, ta del ni več potreben.
        return
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

def zmnozi(mat1, mat2):
    mat = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
    for i in range (0, len(mat1[0])):
        for j in range (0, len(mat1)):
            for k in range (0, len(mat2[0])):
                mat[j][k] += mat1[j][i] * mat2[i][k]
    return mat

def sestej(mat1, mat2):
    mat = [[0 for x in range(len(mat1[0]))] for y in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range (0, len(mat1[0])):
            mat[i][j] = mat1[i][j] + mat2[i][j]
    return mat

def odstej(mat1, mat2):
    mat = [[0 for x in range(len(mat1[0]))] for y in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range (0, len(mat1[0])):
            mat[i][j] = mat1[i][j] - mat2[i][j]
    return mat

import tkinter as tk
from tkinter import *

#-----------------------Pojavno okno----------------------
class prvo_okno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.inv = tk.Button(self.frame, text = "invertiranje", width = 25, command = self.odpri_inv_okno)
        self.inv.pack()
        self.det = tk.Button(self.frame, text = "determinanta", width = 25, command = self.odpri_det_okno)
        self.det.pack()
        self.mnozenje = tk.Button(self.frame, text = "množenje", width = 25, command = self.odpri_mnozenje_okno)
        self.mnozenje.pack()
        self.transponiranje = tk.Button(self.frame, text = "transponiranje", width = 25, command = self.odpri_transponiranje_okno)
        self.transponiranje.pack()
        self.sestevanje = tk.Button(self.frame, text = "seštevanje", width = 25, command = self.odpri_sestevanje_okno)
        self.sestevanje.pack()
        self.TEST = tk.Button(self.frame, text = "TEST", width = 25, command = self.odpri_testno_okno)
        self.TEST.pack()
        self.frame.pack()

    def odpri_testno_okno(self):
        self.odpri_testno_okno = tk.Toplevel(self.master)
        self.app = TESTOkno(self.odpri_testno_okno)
        self.odpri_testno_okno.title("TEST")

    def odpri_inv_okno(self):
        self.odpri_inv_okno = tk.Toplevel(self.master)
        self.app = InvOkno(self.odpri_inv_okno)
        self.odpri_inv_okno.title("Invertiranje")
    
    def odpri_det_okno(self):
        self.odpri_det_okno = tk.Toplevel(self.master)
        self.app = DetOkno(self.odpri_det_okno)
        self.odpri_det_okno.title("Determinanta")

    def odpri_mnozenje_okno(self):
        self.odpri_mnozenje_okno = tk.Toplevel(self.master)
        self.app = MnozenjeOkno(self.odpri_mnozenje_okno)
        self.odpri_mnozenje_okno.title("Množenje")

    def odpri_transponiranje_okno(self):
        self.odpri_transponiranje_okno = tk.Toplevel(self.master)
        self.app = TransponiranjeOkno(self.odpri_transponiranje_okno)
        self.odpri_transponiranje_okno.title("Transponiranje")

    def odpri_sestevanje_okno(self):
        self.odpri_sestevanje_okno = tk.Toplevel(self.master)
        self.app = SestevanjeOkno(self.odpri_sestevanje_okno)
        self.odpri_sestevanje_okno.title("Seštevanje")
#pack in grid ne moreta biti uporabljena hkrati!
class InvOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno = tk.Label(self.frame, text = "Vnesite dimenzijo (kvadratne) matrike:")
        self.tekst_okno.grid(row = 1, column = 1)
        self.vnos = tk.Entry(self.frame, width = 4)
        self.vnos.grid(row = 1, column = 2)
        self.OKgumb = tk.Button(self.frame, text = 'OK', command = self.odpri)
        self.OKgumb.grid(row = 1, column = 3)
        self.racunski_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.izracunaj)
        self.racunski_gumb.grid(row = 2, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.frame.grid()
        
    def odpri(self):
        self.vnosi = []
        dimenzija_matrike = self.vnos.get()
        for vrstica in range(int(dimenzija_matrike)):
            trenutna_vrstica = []
            for stolpec in range(int(dimenzija_matrike)):
                trenutna_vrstica += [tk.Entry(self.frame, width = 2)]
                trenutna_vrstica[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi += [trenutna_vrstica]
        return

    def izracunaj(self):
        matrika = []
        dimenzija_matrike = self.vnos.get()
        for v in range(int(dimenzija_matrike)):
            vrstica = []
            for s in range(int(dimenzija_matrike)):
                vrstica += [float(self.vnosi[v][s].get())]
            matrika += [vrstica]
        self.rez['text']='Inverzna matrika vnešene matrike je ' + str(inverzna(matrika))
        return

    def zapri_okno(self):
        self.master.destroy()

class DetOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno = tk.Label(self.frame, text = "Vnesite dimenzijo (kvadratne) matrike:")
        self.tekst_okno.grid(row = 1, column = 1)
        self.vnos = tk.Entry(self.frame, width = 4)
        self.vnos.grid(row = 1, column = 2)
        self.OKgumb = tk.Button(self.frame, text = 'OK', command = self.odpri)
        self.OKgumb.grid(row = 1, column = 3)
        self.racunski_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.izracunaj)
        self.racunski_gumb.grid(row = 2, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.frame.grid()
        
    def odpri(self):
        self.vnosi = []
        dimenzija_matrike = self.vnos.get()
        for vrstica in range(int(dimenzija_matrike)):
            trenutna_vrstica = []
            for stolpec in range(int(dimenzija_matrike)):
                trenutna_vrstica += [tk.Entry(self.frame, width = 2)]
                trenutna_vrstica[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi += [trenutna_vrstica]
        return

    def izracunaj(self):
        matrika = []
        dimenzija_matrike = self.vnos.get()
        for v in range(int(dimenzija_matrike)):
            vrstica = []
            for s in range(int(dimenzija_matrike)):
                vrstica += [float(self.vnosi[v][s].get())]
            matrika += [vrstica]
        self.rez['text']='Determinanta matrike je ' + str(det(matrika))
        return

    def zapri_okno(self):
        self.master.destroy()

class MnozenjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.input_okno1 = tk.Entry(self.frame)
        self.input_okno1.pack()
        self.tekst_okno1 = tk.Label(self.frame, text = "Vnesite prvo matriko (seznam seznamov):")
        self.tekst_okno1.pack()
        self.input_okno2 = tk.Entry(self.frame)
        self.input_okno2.pack()
        self.tekst_okno2 = tk.Label(self.frame, text = "Vnesite drugo matriko (seznam seznamov):")
        self.tekst_okno2.pack()
        self.racunsko_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.izracunaj)
        self.racunsko_gumb.pack()
        self.rez = tk.Label(self.frame, text = '', )
        self.rez.pack()
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 25, command = self.zapri_okno)
        self.izhodniGumb.pack()
        self.frame.pack()

    def izracunaj(self):
        self.rez['text'] = 'Zmnožek vnešenih matrik je ' + str(zmnozi(pretvorba_niza_v_seznam(self.input_okno1.get()), pretvorba_niza_v_seznam(self.input_okno2.get())))
        return

    def zapri_okno(self):
        self.master.destroy()

class TransponiranjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.input_okno = tk.Entry(self.frame)
        self.input_okno.pack()
        self.tekst_okno = tk.Label(self.frame, text = "Vnesite matriko (seznam seznamov):")
        self.tekst_okno.pack()
        self.racunsko_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.izracunaj)
        self.racunsko_gumb.pack()
        self.rez = tk.Label(self.frame, text = '', )
        self.rez.pack()
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 25, command = self.zapri_okno)
        self.izhodniGumb.pack()
        self.frame.pack()
        
    def izracunaj(self):
        self.rez['text'] = 'Transponirana matrika vnešene matrike je ' + str(transponiraj(pretvorba_niza_v_seznam(self.input_okno.get())))
        return

    def zapri_okno(self):
        self.master.destroy()

class SestevanjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno1 = tk.Label(self.frame, text = "Vnesite matriko (seznam seznamov):")
        self.tekst_okno1.pack()
        self.input_okno1 = tk.Entry(self.frame)
        self.input_okno1.pack()
        self.tekst_okno2 = tk.Label(self.frame, text = "Vnesite matriko (seznam seznamov):")
        self.tekst_okno2.pack()
        self.input_okno2 = tk.Entry(self.frame)
        self.input_okno2.pack()
        self.racunski_gumb = tk.Button(self.frame, text = "Seštej", command = self.sestevanje)
        self.racunski_gumb.pack()
        self.racunski_gumb2 = tk.Button(self.frame, text = "Odštej", command = self.odstevanje)
        self.racunski_gumb2.pack()
        self.rez = tk.Label(self.frame, text = '')
        self.rez.pack()
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 25, command = self.zapri_okno)
        self.izhodniGumb.pack()
        self.frame.pack()

    def sestevanje(self):
        self.rez['text'] = 'Vsota vnešenih matrik je ' + str(sestej(pretvorba_niza_v_seznam(self.input_okno1.get()), pretvorba_niza_v_seznam(self.input_okno2.get())))
        return

    def odstevanje(self):
        self.rez['text'] = 'Razlika vnešenih matrik je ' + str(odstej(pretvorba_niza_v_seznam(self.input_okno1.get()), pretvorba_niza_v_seznam(self.input_okno2.get())))
        return

    def zapri_okno(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = prvo_okno(root)
    root.mainloop()

if __name__ == '__main__':
    main()
