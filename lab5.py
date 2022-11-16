from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open("baby_yoda.jpg")
inic = Image.open("inicialy.bmp")
cpy = im.copy()
cpy2 = im.copy()
cpy3 = im.copy()
cpy4 = im.copy()
cpy5 = im.copy()
cpy6 = im.copy()
cpy7 = im.copy()
cpy8 = im.copy()


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inic(obraz, inicjaly, m, n, kolor):
    w, h = obraz.size
    w_z, h_z = inicjaly.size
    inicArr = np.asarray(inicjaly)

    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            if inicArr[j][i] == False:
                obraz.putpixel((i + m, j + n), kolor)
            else:
                obraz.putpixel((i + m, j + n), (255, 255, 255))

    return obraz


wstaw_inic(cpy, inic, 730, 575, 200).save("obaz1.jpg")


# cpy.show()


def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if inicjaly.getpixel((i, j)) == 0:
            p = obraz.getpixel((i + m, j + n))
            obraz.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    obraz.save("obraz2.jpg")
    # obraz.show()


wstaw_inicjaly_maska(cpy2, inic, 730, 575, 255, 255, 110)


def wstaw_inic_load(obraz, inicjaly, m, n, kolor):
    w, h = obraz.size
    w_z, h_z = inicjaly.size
    ob1 = obraz.load()
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                ob1[i + m, j + n] = kolor

    # obraz.show()


wstaw_inic_load(cpy4, inic, 730, 575, 200)


# cpy4.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    w0, h0 = inicjaly.size
    pix = inicjaly.load()
    pix2 = obraz.load()
    for i, j in zakres(w0, h0):
        if pix[i, j] == 0:
            p = pix2[i + m, j + n]
            pix2[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
    # obraz.show()


wstaw_inicjaly_maska_load(cpy5, inic, 364, 205, 255, 255, 255)


def kontrast(obraz, wsp_kontrastu):
    if 0 <= wsp_kontrastu <= 100:
        mn = ((255 + wsp_kontrastu) / 255) ** 2
        obraz = obraz.point(lambda i: 128 + (i - 128) * mn)
        # obraz.show()
    else:
        print("musi mieścić się w przedziale 0,100")


kontrast(cpy6, 100)


def transformacja_logarytmiczna(obraz):
    obraz = obraz.point(lambda i: 255 * np.log(1 + i / 255))
    # obraz.show()


transformacja_logarytmiczna(cpy7)


def transformacja_gamma(obraz, gamma):
    if gamma > 0:
        obraz = obraz.point(lambda i: (i / 255) ** (1 / gamma) * 255)
        obraz.show()
    else:
        print("gamma < 0")


transformacja_gamma(cpy8, 5)


def zad5(obraz):
    T = np.array(obraz, dtype='uint8')
    T += 100
    obraz_wynik = Image.fromarray(T, "RGB")
    obraz_wynik.show()


zad5(cpy8)


def zad6(obraz):
    obraz = obraz.point(lambda i: i + 100)
    obraz.show()


zad6(cpy8)
