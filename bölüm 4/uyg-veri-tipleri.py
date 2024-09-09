r = float(input("Yarı Çapını Giriniz: "))
piSayisi = 3.14

# Uygulama 1 

alan = piSayisi * (r**2)
cevre = 2 * piSayisi * r

print("Alan: " + str(alan))
print("Çevre: " + str(cevre))

# Uygulama 2 

km = input("Uzunluğu Girin: ")
mil = float((km)) / 1.609344
mil = round(mil, 2) # sayıyı yuvarlamak için 
print("Çevrilen Mil Uzunluğu: " + str(mil) + " mil")