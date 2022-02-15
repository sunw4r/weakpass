#!/usr/bin/env python
import sys
from datetime import datetime

# target variations
company = str(sys.argv[1]).lower()
companyCap = company.capitalize()
companyFullCap = company.upper()

caseTypes = [
    company, 
    companyCap, 
    companyFullCap
]

# numbers variations
currentYear = str(datetime.now().year)
currentYearM = str(datetime.now().year - 1)
currentYearMM = str(datetime.now().year - 2)
currentYearMMM = str(datetime.now().year - 3)
currentYearMMMM = str(datetime.now().year - 4)
currentYearMMMMM = str(datetime.now().year - 5)
currentYearP = str(datetime.now().year + 1)

numbers = [
    currentYear,
    currentYearM,
    currentYearMM,
    currentYearMMM,
    currentYearMMMM,
    currentYearMMMMM,
    currentYearP,
    "1",
    "12",
    "123",
    "1234",
    "12345"
]

# special chars
specials = [
    "@",
    "",
    "!",
    "*",
    "#"
]

# to remove duplicates
wpwdlist = list()


if len(sys.argv) > 2:
    # the big mix
    for x in caseTypes:
        for y in numbers:
            for z in specials:
                wpwdlist.append(x+z+y)
                wpwdlist.append(x+y+z)
                wpwdlist.append(y+x+z)
                wpwdlist.append(y+z+x)
                wpwdlist.append(z+y+x)                
                wpwdlist.append(z+x+y)    
else:
    # the small mix
    for x in caseTypes:
        for y in numbers:
            for z in specials:
                wpwdlist.append(x+z+y)
                wpwdlist.append(x+y+z)
          

output = list(dict.fromkeys(wpwdlist))

for wpwd in output:
    print(wpwd);

#generics
print("Sucesso1!")
print("Sucesso10!")
print("Mudar@123")
print("Mudar123")
print("mudar@123")
print("mudar123")
