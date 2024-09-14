kurum = "BTK AKADEMİ".split()  #str to list demek

print(type(kurum))
print(kurum)
print(kurum[0])
print(kurum[1])

sayilar = [1,2,3,4,5]
isimler = ["ali","ahmet","ayşe"]

print(type(sayilar))
print(type(sayilar[0]))

print(type(isimler))
print(type(isimler[0]))


ogrenci = ["Ertuğrul","Sarsar",60,50,70]

print(ogrenci[0] + " " + ogrenci[1])

ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4]) / 3
print(ortalama)

ogrenciler = [["Ertuğrul","Sarsar",60,50,70],["Ercan","Sarsar",90,80,70]]

print(ogrenciler[0][0])
print(ogrenciler[1][1])
