title = "Python ile Programlama Dersleri"

# 1- "title" değişkeni içerisindeki karakter sayısı nedir?

adet = len(title)
print(adet)


# 2- "title" içerisindeki "python" kelimesini alın

print(title[:6])

# 3- "title" değişkeninin ilk 5 ve son 5 karakterini alın.

print(title[:6])
print(title[-8:])


# 4- "title" değişkenini tersten yazdırınız.

print(title[::-1])

# 5- klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.
# Örnek: Ertuğrul Sarsar isimli öğrencinin 1. Notu 60, 2. Notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

ad = input ("Adı Girin: ")
soyad = input ("Soyadı Girin: ")
not1 = input("1. Not: ")
not2 = input("2. Not: ")
ortalama = (float(not1) + float(not2)) / 2
sonuc = f"{ad} {soyad} isimli öğrencinin 1. Notu 60, 2. Notu 60 ve not ortalaması {ortalama} olarak hesaplanmıştır."
print(sonuc)