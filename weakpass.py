#!/usr/bin/env python
import argparse
import sys
from datetime import datetime

# banner
print('''
          _______  _______  _        _______  _______  _______  _______         _ 
|\     /|(  ____ \(  ___  )| \    /\(  ____ )(  ___  )(  ____ \(  ____ \       / )
| )   ( || (    \/| (   ) ||  \  / /| (    )|| (   ) || (    \/| (    \/   _  / / 
| | _ | || (__    | (___) ||  (_/ / | (____)|| (___) || (_____ | (_____   (_)( (  
| |( )| ||  __)   |  ___  ||   _ (  |  _____)|  ___  |(_____  )(_____  )     | |  
| || || || (      | (   ) ||  ( \ \ | (      | (   ) |      ) |      ) |   _ ( (  
| () () || (____/\| )   ( ||  /  \ \| )      | )   ( |/\____) |/\____) |  (_) \ \ 
(_______)(_______/|/     \||_/    \/|/       |/     \|\_______)\_______)       \_)
                                                                                  
''')

# getting arguments from CLI
parser = argparse.ArgumentParser(description="Weak Pass Suggestions :(")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-b','--big',action='store_true',help="generate more permutations of passwords (recommended for offline brute)")
group.add_argument('-w','--web',action='store_true',help="generate a little amount of permutations (recommended for online spray)")

parser.add_argument('-c','--company',required=True,action='store', type=str,help="Company Name (one word) to be used in permutations")
parser.add_argument('-o','--output',action='store', type=str,help="File to store the passwords. If not specified will show on stdout")

parsed_args = parser.parse_args()

# target variations
company = parsed_args.company.lower()
companyCap = company.capitalize()
companyFullCap = company.upper()

caseTypes = [
    companyCap, 
    company, 
    companyFullCap
]

webCaseTypes = [
    companyCap, 
    company
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

webNumbers = [
    currentYear,
    currentYearM,
    "123"
]

# special chars
specials = [
    "@",
    "",
    "!",
    "*",
    "#"
]

webSpecials = [
    "@",
    ""
]

# to remove duplicates after
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

elif parsed_args.web == True:
    # web mix
    for x in webCaseTypes:
        for y in webNumbers:
            for z in webSpecials:
                wpwdlist.append(x+z+y)
          
output = list(dict.fromkeys(wpwdlist))

# print or save to file
if parsed_args.output:
    with open(parsed_args.output, 'w') as f:
        for wpwd in output:
            f.write(f"{wpwd}\n")
else:
    for wpwd in output:
        print(wpwd);


