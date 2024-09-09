customerName = "Ertugrul"
customerLastName = "Sarsar"
customerPhone = "053212345678"
customerEmail = "ertugrulsarsar@gmail.com"
customerCity = "Bursa"


urun1Ad = "Kablosuz Mouse"
urun1Fiyat = 550

urun2Ad = "Kablosuz Klavye"
urun2Fiyat = 650

urun3Ad = "Dizüstü Bilgisayar"
urun3Fiyat = 55000

kdvOrani = 0.18

toplamUcret = urun1Fiyat + urun2Fiyat + urun3Fiyat
print ("Toplam Ödenen Ücret: " + str(toplamUcret))

print("Toplam Kdv Oranı: " + str(toplamUcret * kdvOrani))



# TypeError: can only concatenate str (not "int") to str (tip hatası)

