# -*- coding: utf-8 -*-

#ogrenci1 = "Engin"
#ogrenci2 = "Derin"
#ogrenci3 = "Salih"
#
#print(ogrenci1)
#print(ogrenci2)
#print(ogrenci3)

ogrenciler = ["Engin","Derin","Salih"]


ogrenciler.append("Ahmet")
#ogrenciler[4] = "Veli"
print(ogrenciler[3])
ogrenciler.remove("Salih")
print(ogrenciler)

#list constructor
sehirler = list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

#diğer fonksiyonlar
#print(sehirler.clear())
print("Ankara sayısı = " + str(sehirler.count("Ankara")))
print("Ankara indexi = " + str(sehirler.index("Ankara")))
sehirler.pop(1)
sehirler.insert(0,"İstanbul")
sehirler.reverse()
print(sehirler)


sehirler3 = sehirler.copy()

sehirler2 = sehirler
sehirler2[0]="İzmir"



print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print(sehirler)



















