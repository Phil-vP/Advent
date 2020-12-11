# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import hashlib

def doSomething():
    
#    with open("input.txt") as fp:
#        allLines = fp.read().splitlines()
    
    input_str = "ckczppom"
#    number = 609043
    
    for i in range(10000000):
        string = input_str + str(i)
        result = hashlib.md5(string.encode())
        
        if str(result.hexdigest())[:6] == "000000":
            print(i)
            break
        
    
    
    print(result.hexdigest())
#    print(int(str(result.hexdigest())[:5]))
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()


if __name__== "__main__":
    doSomething()