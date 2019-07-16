# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi*sayi,sayilar))

#for sayi in sayilar:
#    sayilarKareli.append(sayi*sayi)
    
sayilarFiltreli = list(filter(lambda sayi : sayi>2,sayilar))

    
print(sayilarKareli)
print(sayilarFiltreli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)

print(sayilarFaktoriyel)







