# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:56:01 2020

@author: Philipp
"""

#inputNumber = "59727310424796235189476878806940387435291429226818921130171187957262146115559932358924341808253400617220924411865224341744614706346865536561788244183609411225788501102400269978290670307147139438239865673058478091682748114942700860895620690690625512670966265975462089087644554004423208369517716075591723905075838513598360188150158989179151879406086757964381549720210763972463291801513250953430219653258827586382953297392567981587028568433943223260723561880121205475323894070000380258122357270847092900809245133752093782889315244091880516672127950518799757198383131025701009960944008679555864631340867924665650332161673274408001712152664733237178121872"
#inputNumber = "12345678"
inputNumber = "80871224585914546619083218645595"
numberIter = 100

def doSomething():
    print("in doSomething")
    global inputNumber
    global numberIter
    length = len(inputNumber)*10000
    allMultLists = []
    
    #currentList = list(inputNumber)
    currentList = []
    for x in range(10000):
        currentList.extend(list(inputNumber))
    print("currentList: " + str(currentList))
    
    for x in range(length):
        allMultLists.append(getMultList(length, x+1))
        print("Run " + str(x) + " of " + str(length))
    
    for x in range(numberIter):
        newList = []
        for y in range(length):
            newList.append(getSum(currentList, allMultLists[y]))
        currentList = newList
        #print("currentList nach Durchlauf " + str(x+1) + ": " + str(currentList))
        print("Durchlauf " + str(x))
        
    string = "".join(str(e) for e in currentList)
    print("Complete String:")
    print(string)
    offset = int(string[:7])
    print("offset:")
    print(offset)
    print("Cut String:")
    string = string[offset:]
    print("First Eight:")
    print(string[:8])

def getMultList(maxLen, i):
    liste = []
    x = 0
    while x <= maxLen:
        liste += i*[0]
        if x >= maxLen:
            break
        x += i
        
        liste += i*[1]
        if x >= maxLen:
            break
        x += i
        
        liste += i*[0]
        if x >= maxLen:
            break
        x += i
        
        liste += i*[-1]
        x+= i
    liste = liste[1:(maxLen+1)]
    return liste

def getSum(inputList, multList):
    x = 0
    for i in range(len(inputList)):
        x += int(inputList[i])*int(multList[i])
    return abs(x)%10

if __name__== "__main__":
    doSomething()
    #print(getMultList(10, 1))
    #print(getMultList(10, 2))
    #print(getMultList(10, 3))
    #print(getSum([-4, 5, -1]))