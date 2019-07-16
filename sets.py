# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 13:04:44 2018

@author: Engin
"""

studentsSet = {"Engin","Derin","Salih","Ahmet"}
studentsSet2 = set("Mehmet","Veli","Ayşe")
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Derin" in studentsSet)

if "Derin" in studentsSet:
    print("Listede var")
    

studentsSet.add("Ali")
print(studentsSet)

studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Selin")
print(len(studentsSet))

studentsSet.discard("Selin")
print(len(studentsSet))

x = studentsSet.clear()
print(len(studentsSet))
del studentsSet
print(studentsSet)
















