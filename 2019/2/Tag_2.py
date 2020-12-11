# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

def test():
    print(allInt)
    allInt.append(2)
    allInt.append(3)
    allInt.append(0)
    allInt.append(3)
    print(allInt)
    rechnen(2,3,0,3)
    print(allInt)

def doSomething():
    
    for i in range(50):
        for j in range(50):
    
            with open("input.txt") as fp:
                st = fp.readline()
            
            allInt = st.split(",")
            allInt.pop()
            
            for x in range(len(allInt)):
                allInt[x] = int(allInt[x])
            
            counter = 0
            length = len(allInt)
            maxLength = int(length/4)
            
            #print("length: " + str(length))
            #print("maxLength: " + str(maxLength))
            
            print("Durchlauf " + str(100*i + j))
            
            
            
            allInt[1] = i
            allInt[2] = j
            
            #print(allInt)
            
            while counter < maxLength and allInt[counter*4] != 99:
                index = 4*counter
                i1 = allInt[index+1]
                i2 = allInt[index+2]
                target = allInt[index+3]
                #print(counter)
                if allInt[index] == 1:
                    allInt[target] = allInt[i1] + allInt[i2]
                elif allInt[index] == 2:
                    allInt[target] = allInt[i1] * allInt[i2]
                else:
                    print("ALARM, index ist " + str(index))
                    break
                counter += 1
            
            if(allInt[0] == 19690720):
                print("Lösung!")
                print(i)
                print(j)
                print(str(100*i + j))
                return
    #print(allInt)
    print(length)
    print(maxLength)
    print(allInt[0])
    print("keine Lösung :(")

if __name__== "__main__":
    #test()
    doSomething()