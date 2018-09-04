from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

def novo_okno():
    okno = Toplevel(root)
    okno.title("Matričnik")

def zapri_okno():
    okno = Toplevel(root)
    okno.destroy

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

inv = Button(bottomframe, text = "invertiranje", command = novo_okno)
inv.pack(side = BOTTOM)

det = Button(bottomframe, text = "determinanta", command = novo_okno)
det.pack(side = BOTTOM)

mnozenje = Button(bottomframe, text = "množenje", command = novo_okno)
mnozenje.pack(side = BOTTOM)

transponiranje = Button(bottomframe, text = "transponiranje", command = novo_okno)
transponiranje.pack(side = BOTTOM)

sestevanje = Button(bottomframe, text = "seštevanje", command = novo_okno)
sestevanje.pack(side = BOTTOM)

tr = Button(bottomframe, text = "sled", command = novo_okno)
tr.pack(side = BOTTOM)

izhod = Button(root, text = "Izhod", command = zapri_okno)
izhod.pack()

root.mainloop()
