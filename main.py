from PIL import Image
import numpy as np
obraz = Image.open("inicialy.bmp")
obraz.show()
print("tryb:", obraz.mode)
print("format:", obraz.format)
print("rozmiar:", obraz.size)
dane_obrazka = np.asarray(obraz)
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)
print("adres 50,30:", dane_obrazka[30][50])
print("adres 90,40:", dane_obrazka[40][90])
print("adres 99,0:", dane_obrazka[0][99])
print(dane_obrazka)
dane_obrazka1 = dane_obrazka * 1
t2_text = open('inicialy.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')
print(dane_obrazka1)
ob_d = Image.fromarray(dane_obrazka)
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
ob_d.show()
ob_d1 = Image.fromarray(dane_obrazka1)
print("tryb:", ob_d.mode)
print("format:", ob_d.format)
print("rozmiar:", ob_d.size)
ob_d1.show()
ob_d.save("obraz_zapisany.bmp")
t1 = np.loadtxt("dane.txt", dtype=np.bool_)
print("typ danych tablicy t1:", t1.dtype)
print("rozmiar tablicy t1 :", t1.shape)
print("wymiar tablicy t1 :", t1.ndim)
t2 = np.loadtxt("dane.txt", dtype=np.int_)
print("typ danych tablicy t2:", t2.dtype)
print("rozmiar tablicy t2 :", t2.shape)
print("wymiar tablicy t2 :", t2.ndim)
nowa_t1 = np.loadtxt("dane.txt", dtype=np.bool_)
nowa_t1_1 = nowa_t1 * 1
print(nowa_t1)
print(nowa_t1_1)
porownanie = nowa_t1 == nowa_t1_1
czy_rowne = porownanie.all()
print("czy tablice sa równe? ", czy_rowne)
