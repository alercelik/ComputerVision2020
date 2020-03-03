# kütüphaneleri ekleme
import cv2
import numpy as np

# sys.exit()
import sys

# okuyacağımız dosyayanın path'i
image_path = "../images/itu.jpg"

# fotoğraf okuma fonskiyonu, ikinci parametre okuma modu
#image = cv2.imread(image_path, 1)
image = cv2.imread(image_path) #read as BGR
#image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# image.shape BGR görüntüler için 3 veri döndürür
# Height, Width, Channels = image.shape
print("image dimesions -> {}".format(image.shape))
print("image data type -> {}".format(image.dtype))

print("image height -> {}".format(image.shape[0]))
print("image width -> {}".format(image.shape[1]))
print("image channels -> {}".format(image.shape[2]))

# sırayla:
# "window name" adında bir pencere oluştur ve pencere büyüklüğünü istediğim gibi ayarlayabileyim
# "window name" isimli pencerede image fotoğrafını göster
# benden bir tuş tıklaması gelene kadar bekle
# tüm pencereleri kapat
cv2.namedWindow("window name", cv2.WINDOW_FREERATIO)
cv2.imshow("window name", image)
cv2.waitKey(1000)
cv2.destroyAllWindows()


input("\nPress Enter to continue...\n")

# kaydedeceğimiz dosyayanın ismi dahil path'i
image_write_path = "../images/benim_verecegim_isim.png"

# dikkat, okuduğum görselin formatı .jpg idi, kaydettiğim hali ise .png
cv2.imwrite(image_write_path, image)

input("\nPress Enter to continue...\n")

# piksel bilgilerini printlemek ve değiştirmek için kullanılan komutlar
print("[100, 300]'deki piksel değeri -> {}".format(image[100, 300]))
print("[100, 300]'deki mavi  piksel değeri -> {}".format(image[100, 300, 0]))
print("[100, 300]'deki yeşil   piksel değeri -> {}".format(image[100, 300, 1]))
print("[100, 300]'deki kırmızı    piksel değeri -> {}".format(image[100, 300, 2]))


input("\nPress Enter to continue...\n")

print("Değiştirmeden önce [200, 200] -> {}".format(image[200, 200]))
image[200, 200, 0] = 0
print("Sadece mavi değiştirdikten sonra [200, 200] -> {}".format(image[200, 200]))
image[200, 200] = (100, 100, 100)
print("Hepsini değiştirdikten sonra [200, 200] -> {}".format(image[200, 200]))

input("\nPress Enter to continue...\n")

# convert color (cvtColor) fonksiyonu ile fotoğrafın renk uzayını değiştir. Bizim durumda BGR'dan Gray'e
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image.shape Gray görüntüler için 2 veri döndürür
# Height, Width = image.shape
print("gray_image dimensions-> {}".format(gray_image.shape))

# alttaki ilk kod çalışır ancak ikincisi hata verir, deneyin görün
#print(gray_image[100, 300])
#print(gray_image[100, 300, 0])

cv2.imshow("window2", gray_image)
cv2.waitKey()
cv2.destroyAllWindows()


sys.exit()

# alıştırma - grayscale'a çevirme kodunu kendiniz yazın
# ancak şunu göz önünde bulundurmanız lazım
# gray bir görsel 2 boyutlu, BGR ise 3 boyutludur
# alttaki kodu örnek olarak kullanabilirsiniz

H, W, C = image.shape
# yeni, boş bir görsel oluştur
my_gray = np.zeros((H,W), np.uint8) # unsigned 8-bit'lik integer tipinde HxW'lık boş bir matris oluştur.

# alttaki kodun çok yavaş çalıştığını göreceksiniz. Sebebi for döngüsünü bizim yazmamız diyebiliriz.
for i in range(H):
	for j in range(W):
		# burada gerekli ortalamayı bul ve my_gray'in gerekli yerine eşitle
		#my_gray[i,j] = sum(image[i,j]) // C
		# 0.21R + 0.72G + 0.07B
		my_gray[i,j] = 0.07 * image[i,j,0] + 0.72 * image[i,j,1] + 0.21 * image[i,j,2]


cv2.imshow("my_gray", my_gray)
cv2.waitKey()
cv2.destroyAllWindows()
