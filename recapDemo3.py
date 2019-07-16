# -*- coding: utf-8 -*-

# 2,3,5,7,11,13

sayi = int(input("Sayı giriniz : "))
asalMi = True
for x in range(2,sayi):
    if (sayi % x) == 0:
        asalMi = False
        break

if asalMi:
    print("ASAL")
else:
    print("ASAL DEĞİL")