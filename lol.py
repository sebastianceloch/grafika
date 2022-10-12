from PIL import Image   # Python Imaging Library
import numpy as np

inicjaly = Image.open("inicialy.bmp")
print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)

def wstaw_inicjaly(t_inicjaly,w_m,h_m,wsp):
    h0, w0 = t_inicjaly.shape
    print(h0,w0)
    t = (wsp*h0, wsp*w0)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h_m, h_m + h0 -1):
        for j in range(w_m, w_m + w0-1):
            tab[i][j]=t_inicjaly[i-h_m][j-w_m]
    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    return po_wstawieniu
po_wstawieniu = wstaw_inicjaly(t_inicjaly,50,60,5)
po_wstawieniu.show()

def rysuj_ramke(w, h, dzielnik):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = 1
    tab[grub+grub:z1-grub, grub+grub:z2-grub] = 0
    tab[grub+grub*2:z1-grub*2, grub+grub*2:z2-grub*2] = 0
    tab[grub+grub*3:z1-grub*3, grub+grub*3:z2-grub*3] = 0
    return tab * 255
tab = rysuj_ramke(120, 60, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()

def rysuj_pasy_pionowe(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    print(grub)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    obraz.show()

rysuj_pasy_pionowe(400, 630, 9)



