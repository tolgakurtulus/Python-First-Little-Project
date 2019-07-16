# -*- coding: utf-8 -*-

f = open("musteriler.txt")
#print(f.read())
print("**********")

#print(f.readline())
#print(f.readline())

for l in f:
    print(l)

f.close()

#r Read, a append, w write, x create

fileToAppend = open("ogrenciler.txt","w")
fileToAppend.write("\n")
fileToAppend.write("Ahmet")
fileToAppend.close()

#%%
import os

if os.path.exists("ogrenciler.txt"):    
    os.remove("ogrenciler.txt")
else:
    print("Dosya yok")
    
os.rmdir("empty")















