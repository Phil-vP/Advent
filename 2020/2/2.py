# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()

    count = 0
    
    for line in allLines:
        # print(line)
        line_split = line.split(" ")
        
        first_split = line_split[0].split("-")
        index_1 = int(first_split[0])
        index_2 = int(first_split[1])
        
        letter = line_split[1][:-1]
        
        password = line_split[2]
        
        bool_1 = (password[index_1 - 1] == letter)
        bool_2 = (password[index_2 - 1] == letter)
        
        if bool_1 != bool_2:
            print(password)
            count += 1
    
    print("Final count: " + str(count))
            
    


def aufgabe_a(allLines):
    count = 0
    
    for line in allLines:
        # print(line)
        line_split = line.split(" ")
        
        first_split = line_split[0].split("-")
        minimum = int(first_split[0])
        maximum = int(first_split[1])
        
        letter = line_split[1][:-1]
        
        password = line_split[2]
        
        count_in_pw = password.count(letter)
        
        if minimum <= count_in_pw <= maximum:
            print(password)
            count += 1
        
    
    print("Final count: " + str(count))
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()