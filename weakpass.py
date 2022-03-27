#!/usr/bin/env python
import argparse
import sys
from datetime import datetime

#getting arguments from CLI

parser = argparse.ArgumentParser(description="My parser")
parser.add_argument('-b',"--big",action='store_true',help="generate more permutations of passwords")
parser.add_argument('-c',"--complete",default=False, action='store_true',help="if you generated the small list first, this one will provide missing permutations")
parser.add_argument('-d',required=True,action='store', type=str,help="Domain to be used in permutations")
parsed_args = parser.parse_args()





# target variations
company = parsed_args.d.lower()
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


if (parsed_args.big == True):
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

elif parsed_args.complete == True:

    # completing the mix 

      for x in caseTypes:
        for y in numbers:
            for z in specials:
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
