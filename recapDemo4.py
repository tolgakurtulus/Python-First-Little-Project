# -*- coding: utf-8 -*-

ogrenciler = ["Engin","Derin","Salih","Ali","Ayşe"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()

