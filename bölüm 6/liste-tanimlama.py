programlama_diller = ["Python","C#","Java","Javascript"]

sonuc = programlama_diller
sonuc = type(programlama_diller)
sonuc = programlama_diller[0:3]
sonuc = programlama_diller[-1:]


#güncelleme

programlama_diller[-1] = "Php"
sonuc = programlama_diller

sonuc = len(programlama_diller)
sonuc = programlama_diller + ["Go","Delphi"]

sonuc = "Python" in programlama_diller
sonuc = "React" in programlama_diller



del programlama_diller[0]

for dil in programlama_diller:
    print(dil)



print(sonuc)