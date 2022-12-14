from PIL import Image, ImageChops
import matplotlib.pyplot as plt

obraz1 = Image.open("obraz.png")
r,g,b,a = obraz1.split()
obraz2 = obraz1.copy().convert("RGB")
obraz3 = Image.new("RGB",obraz2.size,(255,255,255))
obraz3.paste(obraz1)
obraz3.save("obraz3.png")
ImageChops.difference(obraz2,obraz3).show()

cmyk = obraz3.convert("CMYK")
ycbcr = obraz3.convert("YCbCr")
hsv =  obraz3.convert("HSV")

plt.figure(figsize=(32,16))
plt.subplot(1,3,1)
plt.axis("off")
plt.title("CMYK")
plt.imshow(cmyk)
plt.subplot(1,3,2)
plt.axis("off")
plt.title("YCbCr")
plt.imshow(ycbcr)
plt.subplot(1,3,3)
plt.axis("off")
plt.title("HSV")
plt.imshow(hsv)
#plt.show()

cmyk2 = obraz3.copy().convert("CMYK")
ycbcr2 = obraz3.copy().convert("YCbCr")
hsv2 = obraz3.copy().convert("HSV")

c,m,y,k = cmyk2.split()
y,Cb,Cr = ycbcr2.split()
h,s,v = hsv2.split()

plt.figure(figsize=(8,4))
plt.subplot(2,2,1)
plt.axis("off")
plt.title("c")
plt.imshow(c,"gray")
plt.subplot(2,2,2)
plt.axis("off")
plt.title("m")
plt.imshow(m,"gray")
plt.subplot(2,2,3)
plt.axis("off")
plt.title("y")
plt.imshow(y,"gray")
plt.subplot(2,2,4)
plt.axis("off")
plt.title("k")
plt.imshow(k,"gray")
plt.show()
plt.savefig("cmyk.png")

plt.figure(figsize=(8,4))
plt.subplot(1,3,1)
plt.axis("off")
plt.title("y")
plt.imshow(y,"gray")
plt.subplot(1,3,2)
plt.axis("off")
plt.title("Cb")
plt.imshow(Cb,"gray")
plt.subplot(1,3,3)
plt.axis("off")
plt.title("Cr")
plt.imshow(Cr,"gray")
plt.show()
plt.savefig("ycbcr")

plt.figure(figsize=(8,4))
plt.subplot(1,3,1)
plt.axis("off")
plt.title("h")
plt.imshow(h,"gray")
plt.subplot(1,3,2)
plt.axis("off")
plt.title("s")
plt.imshow(s,"gray")
plt.subplot(1,3,3)
plt.axis("off")
plt.title("v")
plt.imshow(v,"gray")
plt.show()
plt.savefig("hsv")


obraz4 = Image.open("Shrek_Fiona.png").resize(obraz1.size,1)
obraz4_copy = obraz4.copy()
obraz1_copy = obraz1.copy()
obraz4_copy.paste(obraz1,mask=a)
obraz1_copy.paste(obraz4,mask=a)
plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title("Obraz 1 w obraz 4")
plt.imshow(obraz4_copy,"gray")
plt.axis("off")
plt.subplot(1,2,2)
plt.title("Obraz 4 w obraz 1")
plt.imshow(obraz1_copy,"gray")
plt.axis("off")
plt.show()
plt.savefig("fig2.png")

