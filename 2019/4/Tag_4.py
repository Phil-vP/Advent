# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

def test(number):
    double = False
    #print(number)
    for i in range(5):
        j = i+2
        n = str(number)[i:j]
        #print(n)
        if(int(n[0]) > int(n[1])):
            return False
        if(n[0] == n[1]):
            double = True
    return(double)
    
def testTwo(number):
    double = False
    multiple = False
    stNumber = str(number)
    for i in range(5):
        j = i+2
        n = stNumber[i:j]
        #print(n)
        if(int(n[0]) > int(n[1])):
            return False
        
    arr = [False]*6
    
    for x in range(5):
        if not arr[x]:
            #print("In x=" + str(x))
            maxLen = 1
            length = 1
            while x < 5 and stNumber[x] == stNumber[x+1]:
                arr[x+1] = True
                x += 1
                length += 1
            if length > maxLen:
                maxLen = length
                #print(maxLen)
                #print("---")
            if maxLen == 2:
                double = True
    return double

if __name__== "__main__":
    
    #print(testTwo(112233))
    #print(testTwo(123444))
    #print(testTwo(111122))
    
    counter = 0
    
    for x in range(254032, 789860):
        if testTwo(x):
            counter += 1
    
    print(counter)
    