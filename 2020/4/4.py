# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import re

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
#    print(allLines)
    
    validCounter = 0
    
    passport = {}
    
    for l in allLines:
        if l == '':
            validCounter += checkValidAndPresent(passport)
            passport  = {}
            continue
        
        l_sp = l.split(' ')
        
        for s in l_sp:
            s_sp = s.split(':')
            passport[s_sp[0]] = s_sp[1]
    
    validCounter += checkValidAndPresent(passport)
    
    print(validCounter)
    
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

def checkBYR(byr):
    return 1920 <= byr <= 2002

def checkIYR(iyr):
    return 2010 <= iyr <= 2020

def checkEYR(eyr):
    return 2020 <= eyr <= 2030

def checkHGT(hgt):
    if not "in" in hgt and not "cm" in hgt:
        print("neither inch nor centimeter")
        return False
    
    hgt_number = int(hgt[:-2])
    hgt_index = hgt[-2:]
    
    if hgt_index == "in":
        if not 59 <= hgt_number <= 76:
            print("hgt inch invalid: " + str(hgt_number))
            return False
    
    else:
        if not 150 <= hgt_number <= 193:
            print("hgt centimeter invalid: " + str(hgt_number))
            return False    
    
    return True

def checkHCL(hcl):
    return re.match('^#[[a-f\d]{6}', hcl) != None

def checkECL(ecl):
    all_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in all_ecl

def checkPID(pid):
    return re.match('\d{9}$', pid) != None

def checkValidAndPresent(passport):
    keys = list(passport.keys())
    keys.sort()
    
    if len(keys) <= 6:
        print("Too few keys: " + str(keys) + "\n")
        return 0
    if len(keys) == 7 and "cid" in keys:
        print("Too few keys with cid: " + str(keys) + "\n")
        return 0
    
    byr = int(passport["byr"])
    iyr = int(passport["iyr"])
    eyr = int(passport["eyr"])
    hgt = passport["hgt"]
    hcl = passport["hcl"]
    ecl = passport["ecl"]
    pid = passport["pid"]
    
    if not checkBYR(byr):
        print("byr " + str(byr) + " invalid\n")
        return 0
    
    if not checkIYR(iyr):
        print("iyr " + str(iyr) + " invalid\n")
        return 0
    
    if not checkEYR(eyr):
        print("eyr " + str(eyr) + " invalid\n")
        return 0
    
    if not checkHGT(hgt):
        print("hgt " + hgt + " invalid\n")
        return 0
    
    if not checkHCL(hcl):
        print("hcl doesn't match: " + hcl + "\n")
        return 0
    
    if not checkECL(ecl):
        print("ecl doesn't match: " + ecl + "\n")
        return 0
    
    if not checkPID(pid):
        print("pid doesn't match: " + pid + "\n")
        return 0
    
    
    return 1
    
    

def checkValid(passport):
    keys = list(passport.keys())
    
#    for k in keys:
#        print(k + ": " + passport[k])
#    print()
    
    if len(keys) == 8:
        return 1
    
    if len(keys) == 7 and not "cid" in keys:
        return 1
    
    return 0

def testing():
    print(checkBYR(2002))
    print(checkBYR(2003))
    
    print()
    
    print(checkHGT("60in"))
    print(checkHGT("190cm"))
    print(checkHGT("190in"))
    print(checkHGT("190"))
    
    print()
    
    print(checkHCL("#123abc"))
    print(checkHCL("#123abz"))
    print(checkHCL("123abc"))
    
    print()
    
    print(checkECL("brn"))
    print(checkECL("wat"))
    
    print()
    
    print(checkPID("000000001"))
    print(checkPID("0123456789"))

if __name__== "__main__":
#    testing()
    doSomething()