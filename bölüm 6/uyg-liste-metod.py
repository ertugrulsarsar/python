customer = ["ertugrulsarsar","ercansarsar","sakinesarsar","sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
orderTotals = [10000,12000,15000,60000,45000,30000,5000]

#1-"ertugrulsarsar"  kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekle

customer.append("ertugrulsarsar")
orderTotals.append(5000)

sonuc = customer
sonuc = orderTotals

#2- son eklenen sipairşi sil

sonuc = customer.pop()
sonuc = orderTotals.pop()


#3- Tüm müşteriler için aşağıdaki özet cümleyi yazdır
    #"<username>" isimli müşterinin sipariş toplamı "<10000>" liradır

sonuc = f" {customer[0]}isimli müşterinin sipariş toplamı {orderTotals[3]}  liradır"



#4- müşterileri alfabetik olarak sırala

customer.sort()
print(customer)

#5- sipariş toplamlarını azalan şekilde sırala

orderTotals.sort
orderTotals.reverse()


#6- en düşük sipariş hangisi

sonuc = min(orderTotals)
sonuc = max(orderTotals)

#7- "ertugrulsarsar" isimli kullanıcının kaç tane siparişi vardır

sonuc = customer.count("ertugrulsarsar")


#8- customer listesinden "sakinesarsar" isimli kullanıcıyı sil

customer.remove("sakinesarsar")
sonuc = customer

#9- listelerdeki tüm içerikleri sil

customer.clear()
orderTotals.clear()

sonuc = customer

#10- kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekle

userName = input("Müşteri Adı: ")
toplam = input("Toplam: ")

customer.append(userName)
orderTotals.append(orderTotals)

print(customer)
print(orderTotals)

