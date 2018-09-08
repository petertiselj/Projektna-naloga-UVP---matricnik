#input je vedno string (niz), zato za začetni program kmečka funkija, ki pretvori takšen input v seznam
#ko input postane grafičen - vnašanje vrednosti v entry widgete, te funkcije ne potrebujemo več
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

def zaokrozi(matrika):
    for v in range(len(matrika)):
        for s in range(len(matrika[0])):
            matrika[v][s] = round(matrika[v][s], 2)
    return matrika

import tkinter as tk
from tkinter import *

#---------------------------Pojavno okno---------------------------
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
        self.frame.pack()

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
        self.racunski_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.preberi_in_izracunaj)
        self.racunski_gumb.grid(row = 2, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 7, command = self.zapri_okno)
        self.izhodniGumb.grid(column = 1)
        self.frame.grid()        
        
#funkcija odpri poveže vnosna polja in jih zloži v matriko, da te vrednosti nato lahko preberemo     
    def odpri(self):
        if hasattr(self, 'vnosi'):
            for v in range(len(self.vnosi)):
                for s in range(len(self.vnosi)):
                    self.vnosi[v][s].grid_forget()
            self.rez['text'] = ''
        self.vnosi = []
        dimenzija_matrike = self.vnos.get()
        for vrstica in range(int(dimenzija_matrike)):
            trenutna_vrstica = []
            for stolpec in range(int(dimenzija_matrike)):
                trenutna_vrstica += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi += [trenutna_vrstica]
        return
    
#najprej naredi matriko iz vnešenih vrednosti, nato pa še izračuna inverz
    def preberi_in_izracunaj(self):
        matrika = []
        dimenzija_matrike = self.vnos.get()
        for v in range(int(dimenzija_matrike)):
            vrstica = []
            for s in range(int(dimenzija_matrike)):
                vrstica += [float(self.vnosi[v][s].get())]
            matrika += [vrstica]
        if det(matrika) == 0:
            self.rez['text'] = 'Vaša matrika ni obrnljiva - je singularna.'
        else:
            self.rez['text'] = 'Inverzna matrika vnešene matrike je ' + str(zaokrozi(inverzna(matrika)))
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
        self.racunski_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.preberi_in_izracunaj)
        self.racunski_gumb.grid(row = 2, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 7, command = self.zapri_okno)
        self.izhodniGumb.grid(column = 1)
        self.frame.grid()
        
    def odpri(self):
        self.vnosi = []
        dimenzija_matrike = self.vnos.get()
        for vrstica in range(int(dimenzija_matrike)):
            trenutna_vrstica = []
            for stolpec in range(int(dimenzija_matrike)):
                trenutna_vrstica += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi += [trenutna_vrstica]
        return

    def preberi_in_izracunaj(self):
        matrika = []
        dimenzija_matrike = self.vnos.get()
        for v in range(int(dimenzija_matrike)):
            vrstica = []
            for s in range(int(dimenzija_matrike)):
                vrstica += [float(self.vnosi[v][s].get())]
            matrika += [vrstica]
        self.rez['text'] = 'Determinanta matrike je ' + str(round(det(matrika), 3))
        return

    def zapri_okno(self):
        self.master.destroy()

class MnozenjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno1 = tk.Label(self.frame, text = "Vnesite dimenzijo prve matrike, št. vrstic:")
        self.tekst_okno1.grid(row = 1, column = 1)
        self.vnos1 = tk.Entry(self.frame, width = 4)
        self.vnos1.grid(row = 1, column = 2)
        self.tekst_okno2 = tk.Label(self.frame, text = "št. stolpcev:")
        self.tekst_okno2.grid(row = 1, column = 3)
        self.vnos2 = tk.Entry(self.frame, width = 4)
        self.vnos2.grid(row = 1, column = 4)
        self.OKgumb1 = tk.Button(self.frame, text = 'OK', command = self.odpri1)
        self.OKgumb1.grid(row = 1, column = 5)
        self.racunski_gumb1 = tk.Button(self.frame, text = "Zmnoži", command = self.preberi_in_zmnozi)
        self.racunski_gumb1.grid(row = 3, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 3, column = 1)
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 7, command = self.zapri_okno)
        self.izhodniGumb.grid(column = 1)
        self.frame.grid()

    def odpri1(self):
        self.tekst_okno3 = tk.Label(self.frame, text = "Vnesita dimenzijo druge matrike, št. vrstic:")
        self.tekst_okno3.grid(row = 2, column = 1)
        self.tekst_okno4 = tk.Label(self.frame, text = str(self.vnos2.get()))
        self.tekst_okno4.grid(row = 2, column = 2)
        self.tekst_okno5 = tk.Label(self.frame, text = "št. stolpcev:")
        self.tekst_okno5.grid(row = 2, column = 3)
        self.vnos3 = tk.Entry(self.frame, width = 4)
        self.vnos3.grid(row = 2, column = 4)
        self.OKgumb2 = tk.Button(self.frame, text = 'OK', command = self.odpri2)
        self.OKgumb2.grid(row = 2, column = 5)
        return

    def odpri2(self):
        self.vnosi1 = []
        self.vnosi2 = []
        vrstice1 = int(self.vnos1.get())
        stolpci1 = int(self.vnos2.get())
        vrstice2 = int(self.vnos2.get())
        stolpci2 = int(self.vnos3.get())
        for vrstica in range(vrstice1):
            trenutna_vrstica1 = []
            for stolpec in range(stolpci1):
                trenutna_vrstica1 += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica1[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi1 += [trenutna_vrstica1]
            self.vmesno = tk.Label(self.frame, text = '  ')
            self.vmesno.grid(row = vrstica + 4, column = stolpci1 + 4)
        for vrstica in range(vrstice2):
            trenutna_vrstica2 = []
            for stolpec in range(stolpci2):
                trenutna_vrstica2 += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica2[stolpec].grid(row = vrstica + 4, column = stolpec + stolpci1 + 5)
            self.vnosi2 += [trenutna_vrstica2]
        return

    def preberi_in_zmnozi(self):
        matrika1 = []
        vrstice1 = int(self.vnos1.get())
        stolpci1 = int(self.vnos2.get())
        vrstice2 = int(self.vnos2.get())
        stolpci2 = int(self.vnos3.get())
        for v in range(vrstice1):
            vrstica = []
            for s in range(stolpci1):
                vrstica += [float(self.vnosi1[v][s].get())]
            matrika1 += [vrstica]
        matrika2 = []
        for v in range(vrstice2):
            vrstica = []
            for s in range(stolpci2):
                vrstica += [float(self.vnosi2[v][s].get())]
            matrika2 += [vrstica]
        self.rez['text'] = 'Zmnožek matrik je ' + str(zaokrozi(zmnozi(matrika1, matrika2)))
        return

    def zapri_okno(self):
        self.master.destroy()

class TransponiranjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno1 = tk.Label(self.frame, text = "Vnesite dimenzijo matrike, št. vrstic:")
        self.tekst_okno1.grid(row = 1, column = 1)
        self.vnos1 = tk.Entry(self.frame, width = 4)
        self.vnos1.grid(row = 1, column = 2)
        self.tekst_okno2 = tk.Label(self.frame, text = "št. stolpcev:")
        self.tekst_okno2.grid(row = 1, column = 3)
        self.vnos2 = tk.Entry(self.frame, width = 4)
        self.vnos2.grid(row = 1, column = 4)
        self.OKgumb = tk.Button(self.frame, text = 'OK', command = self.odpri)
        self.OKgumb.grid(row = 1, column = 5)
        self.racunski_gumb = tk.Button(self.frame, text = "Izračunaj", command = self.preberi_in_izracunaj)
        self.racunski_gumb.grid(row = 2, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 7, command = self.zapri_okno)
        self.izhodniGumb.grid(column = 1)
        self.frame.grid()
        
    def odpri(self):
        self.vnosi = []
        vrstice = int(self.vnos1.get())
        stolpci = int(self.vnos2.get())
        for vrstica in range(vrstice):
            trenutna_vrstica = []
            for stolpec in range(stolpci):
                trenutna_vrstica += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi += [trenutna_vrstica]
        return

    def preberi_in_izracunaj(self):
        matrika = []
        vrstice = int(self.vnos1.get())
        stolpci = int(self.vnos2.get())
        for v in range(vrstice):
            vrstica = []
            for s in range(stolpci):
                vrstica += [float(self.vnosi[v][s].get())]
            matrika += [vrstica]
        self.rez['text'] = 'Transponiranka vnešene matrike je ' + str(zaokrozi(transponiraj(matrika)))
        return

    def zapri_okno(self):
        self.master.destroy()

class SestevanjeOkno:
    
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.tekst_okno1 = tk.Label(self.frame, text = "Vnesite dimenzijo matrike, št. vrstic:")
        self.tekst_okno1.grid(row = 1, column = 1)
        self.vnos1 = tk.Entry(self.frame, width = 4)
        self.vnos1.grid(row = 1, column = 2)
        self.tekst_okno2 = tk.Label(self.frame, text = "št. stolpcev:")
        self.tekst_okno2.grid(row = 1, column = 3)
        self.vnos2 = tk.Entry(self.frame, width = 4)
        self.vnos2.grid(row = 1, column = 4)
        self.OKgumb = tk.Button(self.frame, text = 'OK', command = self.odpri)
        self.OKgumb.grid(row = 1, column = 5)
        self.racunski_gumb1 = tk.Button(self.frame, text = "Seštej", command = self.preberi_in_sestej)
        self.racunski_gumb1.grid(row = 2, column = 3)
        self.racunski_gumb2 = tk.Button(self.frame, text = "Odštej", command = self.preberi_in_odstej)
        self.racunski_gumb2.grid(row = 3, column = 3)
        self.rez = tk.Label(self.frame, text = '')
        self.rez.grid(row = 2, column = 1)
        self.izhodniGumb = tk.Button(self.frame, text = 'Zapri', width = 7, command = self.zapri_okno)
        self.izhodniGumb.grid(column = 1)
        self.frame.grid()

    def odpri(self):
        self.vnosi1 = []
        self.vnosi2 = []
        vrstice = int(self.vnos1.get())
        stolpci = int(self.vnos2.get())
        for vrstica in range(vrstice):
            trenutna_vrstica1 = []
            for stolpec in range(stolpci):
                trenutna_vrstica1 += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica1[stolpec].grid(row = vrstica + 4, column = stolpec + 4)
            self.vnosi1 += [trenutna_vrstica1]
            self.vmesno = tk.Label(self.frame, text = '  ')
            self.vmesno.grid(row = vrstica + 4, column = stolpci + 4)
            trenutna_vrstica2 = []
            for stolpec in range(stolpci):
                trenutna_vrstica2 += [tk.Entry(self.frame, width = 5)]
                trenutna_vrstica2[stolpec].grid(row = vrstica + 4, column = stolpec + stolpci + 5)
            self.vnosi2 += [trenutna_vrstica2]
        return

    def preberi_in_sestej(self):
        matrika1 = []
        vrstice = int(self.vnos1.get())
        stolpci = int(self.vnos2.get())
        for v in range(vrstice):
            vrstica = []
            for s in range(stolpci):
                vrstica += [float(self.vnosi1[v][s].get())]
            matrika1 += [vrstica]
        matrika2 = []
        for v in range(vrstice):
            vrstica = []
            for s in range(stolpci):
                vrstica += [float(self.vnosi2[v][s].get())]
            matrika2 += [vrstica]
        self.rez['text'] = 'Vsota matrik je ' + str(zaokrozi(sestej(matrika1, matrika2)))
        return

    def preberi_in_odstej(self):
        matrika1 = []
        vrstice = int(self.vnos1.get())
        stolpci = int(self.vnos2.get())
        for v in range(vrstice):
            vrstica = []
            for s in range(stolpci):
                vrstica += [float(self.vnosi1[v][s].get())]
            matrika1 += [vrstica]
        matrika2 = []
        for v in range(vrstice):
            vrstica = []
            for s in range(stolpci):
                vrstica += [float(self.vnosi2[v][s].get())]
            matrika2 += [vrstica]
        self.rez['text'] = 'Razlika matrik je ' + str(zaokrozi(odstej(matrika1, matrika2)))
        return

    def zapri_okno(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = prvo_okno(root)

    root.mainloop()

if __name__ == '__main__':
    main()
