# string concat

ad = "Ertuğrul"
soyad = "Sarsar"
yas = 30

# msj = ("Benim adım " + ad + " " + soyad + "." + str(yas) + "yasindayım")

# msj = "Benim adım {} {}. {} yaşındayım".format(ad, soyad, yas)



#string format
# msj = "Benim adım {} {}. {} yaşındayım".format(ad, soyad, yas)
msj = "Benim adım {1} {0}.{1} {2} yaşındayım".format(ad, soyad, yas)
msj = "Benim adım {a} {s}. {y} yaşındayım".format(a=ad, s=soyad, y=yas)



# f-string
msj = f"Benim adım {ad} {soyad}. {yas} yaşındayım"




print (msj)