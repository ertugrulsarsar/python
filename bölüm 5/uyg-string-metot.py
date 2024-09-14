kursAdi ="Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

#1 ' Btk Akademi ' karakter dizisinin baş ve sondaki boşluk karakterlerini siliniz.


sonuc = ' Btk Akademi '.strip()


#2 kursAdi değişkenindeki tüm karakterleri küçük harfa çevir.

sonuc = kursAdi.lower()

#3 website değişkeninde kaç tane '.' karakteri vardır?

sonuc = website.count(".")

#4 website değişkeni 'https' ile mi başlıyor

sonuc = website.startswith("https")

#5 website 'tr' ile mi bitiyor

sonuc = website.endswith("tr")

#6 kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor

sonuc = kursAdi.isalpha()

#7 kursAdi değişkenindeki tüm boşukları '-' ile değiştir.

sonuc = kursAdi.replace(" ","-")

#8 kursAdi değişkenindeki Python kelimesini ReactJs ile değiştir.

sonuc = kursAdi.replace("Python","ReactJs")

#9 website değişkeni 'www' içeriyor mu?

sonuc = website.find("www")

#10 kursAdi değişkenini listeye çevir

sonuc = kursAdi.split()
















print(sonuc)