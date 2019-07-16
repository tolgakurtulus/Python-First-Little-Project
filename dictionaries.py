# -*- coding: utf-8 -*-

sozluk = {
        "book" : "kitap",
        "table" : "masa"
        }

sozluk2 = dict(kitap ="book", masa = "table")

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
del(sozluk["book"])
print(len(sozluk))

