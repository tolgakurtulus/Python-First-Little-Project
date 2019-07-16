# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:48:42 2018

@author: Engin
"""

import json

data = '{"firstName":"engin","lastName":"demiroğ"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])


customer = {
        "firstName":"engin",
        "email":"engindemirog@gmail.com"
        }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))
