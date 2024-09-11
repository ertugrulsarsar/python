kurs = "Python ile Programlama"

print(kurs[0])      # p 
print(kurs[-1])     # a

adet = len(kurs)    #karakter sayısını verir
print(adet)
# print(kurs[adet])   #hatalı kod

# IndexError: string index out of range (sınırları aştı hatası)

print(kurs[adet-1])

print(kurs[0:6])            # python
print(kurs[:6])             # python

print(kurs[11:22])          # programlama
print(kurs[11:len(kurs)])   # programlama
print(kurs[5:])             # programlama

print(kurs[-12:-1])         # programlam

print(kurs[0:20:3])         # adım sayısı

print(kurs[::-1])           # amalmargorP eli nohtyP

