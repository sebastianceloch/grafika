from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


im = Image.open('baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)
im1=im.copy()
im2=im.copy()
def rysuj_prostokat(obraz,m,n,a,b,kolor):
    for i in range(a):
        obraz.putpixel((i+m,n),kolor)
        obraz.putpixel((i + m,n+b), kolor)
        for j in range(b):
            obraz.putpixel((m,j+n), kolor)
            obraz.putpixel((m+a,j+n),kolor)
    return obraz
rysuj_prostokat(im1,25,30,100,100,(255,0,0)).show()
def rysuj_kwadrat(obraz,m,n,a,kolor):
    for i in range(a):
        obraz.putpixel((i+m,n),kolor)
        obraz.putpixel((i + m,n+a), kolor)
        for j in range(a):
            obraz.putpixel((m,j+n), kolor)
            obraz.putpixel((m+a,j+n),kolor)
    return obraz
rysuj_kwadrat(im2,25,30,100,(255,0,0)).show()
def odbij_gora_dol(im):
    img = im.copy()
    w, h = im.size
    w1 = int(h / 2)
    px = img.load()
    for i in range(h, w1):
        for j in range(h):
            px[i, j] = px[w, j-i]
    return img
odbij_gora_dol(im)