# -*- coding: utf-8 -*-
import sys

liste = [7,'engin',0,3,"6"]

for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç : " + str(sonuc))
    except ValueError:
        print(str(x)+ " bir sayı değil")
    except ZeroDivisionError:
        print(str(x)+ " için sıfıra bölme hatası")
    except:
        print(str(x) +" hesaplanamadı")
        print("Sistem diyor ki : " + str(sys.exc_info()[0]))
    finally:
        print("İşlemler bitti")
        
   
try:
    file = open("abc.txt")
except:
    print("dosya hatası")
finally:
    file.close()
    print("dosya kapandı")
    
    
    
    
    
    
        
    