from PIL import Image   # Python Imaging Library
import numpy as np

def rysuj_ramke(w, h, dzielnik,kolor,kolor_ramki):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[:] = kolor
    tab[grub:z1, grub:z2] = kolor_ramki
    tab[grub+grub:z1-grub, grub+grub:z2-grub] = kolor
    tab[grub+grub*2:z1-grub*2, grub+grub*2:z2-grub*2] = kolor_ramki
    tab[grub+grub*3:z1-grub*3, grub+grub*3:z2-grub*3] = kolor
    return tab * 255
tab = rysuj_ramke(120, 60, 8,100,200)
im_ramka = Image.fromarray(tab)
#im_ramka.show()
tab_rysuj = rysuj_ramke(480,320,8,100,200)
rysuj = Image.fromarray(tab_rysuj)


def zad4(w,h,kolor,kolor_ramki):
    t=(h,w)
    tab = np.zeros(t, dtype=np.uint8)
    tab[:] = kolor
    tab[0:int(h/2),0:int(w/2)]=kolor_ramki
    tab[int(h/2):h,int(w/2):w]=kolor_ramki
    return tab*255
tab = zad4(480,320,100,200)
in_ramka = Image.fromarray(tab)
#in_ramka.show()

def rysuj_pasy_poziome_kolor(w, h, dzielnik, kolor,
                             zmiana_koloru):  # funkcja rysuje pasy poziome, przy czym kazda składowa koloru zwieksza się o "zmiana_koloru"
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        r = (kolor[0] + k * zmiana_koloru) % 255
        g = (kolor[1] + k * zmiana_koloru) % 255
        b = (kolor[2] + k * zmiana_koloru) % 255
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                tab[i,j] = [r, g, b]
    return tab

tab1 = rysuj_pasy_poziome_kolor(300, 200, 20, [100, 200, 0], 32)
obraz1 = Image.fromarray(tab1)
obraz1.show()

#negatyw to 255-kolor ktory chce sie znegatywowac np [100,200,100] = [255-100,255-200,255-100]
def zad3(w,h):
    print(w)