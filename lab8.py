from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow,ImageFilter
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

def statystyki(im):
    s = stat.Stat(im)
    print("Przedział wartości pikseli ", s.extrema)  # max i min
    print("Liczba piskeli ", s.count)  # zlicza
    print("Średnia wartość pikseli ", s.mean)  # srednia
    print("Mediana wartości pikseli ", s.median)  # mediana
    print("Odchylenie standardowe pikseli", s.stddev)  # odchylenie standardowe


obraz = Image.open("brain.png")
print(obraz.mode)
obraz=obraz.convert("L")
hist = obraz.histogram()
statystyki(obraz)
print(hist)

def histogram_norm(obraz):
    s = stat.Stat(obraz)
    hist=obraz.histogram()
    hist_norm = []
    for i in hist:
        hist_norm.append(i/s.count[0])
    return hist_norm

def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_kumul=[]
    pom = np.cumsum(hist_norm)
    for i in pom:
        hist_kumul.append(i)
    return hist_kumul

def histogram_equalization(obraz):
    pom = np.asarray(obraz)
    hist_kumul = histogram_cumul(obraz)
    obraz_list = list(pom.flatten())
    equalization_list = [int(hist_kumul[p]*255) for p in obraz_list]
    equalization_list_array = np.reshape(np.asarray(equalization_list),pom.shape)
    obraz_equalization = Image.fromarray(equalization_list_array)
    hist_equalization = obraz_equalization.histogram()
    return hist_equalization

plt.figure(figsize=(8,6))
plt.subplot(2,2,1)
plt.title("Histogram")
plt.plot(range(256), hist[:256], color='b', alpha=1)
plt.subplot(2,2,2)
plt.title("znormalizowany")
plt.plot(range(256), histogram_norm(obraz)[:256], color='b', alpha=1)
plt.subplot(2,2,3)
plt.title("skumulowany")
plt.plot(range(256), histogram_cumul(obraz)[:256], color='b', alpha=1)
plt.subplot(2,2,4)
plt.title("equalization")
plt.bar(range(256),histogram_equalization(obraz)[:256], color='b', alpha=1)
plt.show()

plt.figure(figsize=(32,16))
plt.subplot(1,1,1)
plt.title("Histogram po wyrónaniu")
plt.bar(range(256),histogram_equalization(obraz)[:256], color='b', alpha=1)
plt.savefig("equalized.png")
plt.show()

im_equalized1 = ImageOps.equalize(obraz, mask=None)
im_equalized1.save("equalized1.png")

plt.figure(figsize=(32,16))
plt.subplot(1,2,1)
plt.title("Histogram po wyrónaniu(funckja)")
plt.bar(range(256),histogram_equalization(obraz)[:256], color='b', alpha=1)
plt.subplot(1,2,2)
plt.title("Histogram po wyrónaniu(ImageChops.equalize)")
plt.bar(range(256),im_equalized1.histogram())
plt.show()