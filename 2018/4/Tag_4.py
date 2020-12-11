# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:32:15 2020

@author: Philipp
"""
#import collections

testing = False


def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    with open(name) as f:
        allLines = f.readlines()
    
    for c in range(len(allLines)):
        allLines[c] = allLines[c].rstrip()
    
    days = {}
    for l in allLines:
        l2 = l.split("]")
        line = l2[0].split(" ")
        d = line[0][1:]
        print(d)
        if d not in days:
            days[d] = {}
        #days[d][line[1][:-1]] = line[2:]
        days[d][line[1]] = l2[1]
    
    #for d in days:
        #print(d + ":")
        #print(days[d])
        #days[d] = collections.OrderedDict(sorted(days[d].items()))
    
    print()
    
    for d in days:
        print(d + ":")
        print(days[d])
    
    print("------------------------------")
    print("Sorting...")
    
    allDays = {}
    sortedKeys = sorted(days.keys())
    for key in sortedKeys:
        allDays[key] = days[key]
    
    
    keyList = list(allDays.keys())
    print(keyList)
    for k in range(len(keyList)):
        #print(allDays[keyList[k]])
        timeList = list(allDays[keyList[k]].keys())
        for x in range(len(timeList)):
            if "23:" in timeList[x]:
                allDays[keyList[k+1]]["00:00"] = allDays[keyList[k]][timeList[x]]
                del allDays[keyList[k]][timeList[x]]
                
    
    for d in allDays:
        k = allDays[d].keys()
        liste = sorted(k)
        unsorted = allDays[d]
        day = {}
        for key in liste:
            day[key] = unsorted[key]
        allDays[d] = day
    
    print("------------------------------")
    
    for d in allDays:
        print(d + ":")
        for t in allDays[d]:
            print(t + ":" + str(allDays[d][t]))

    allGuards = {}
    allGuardsTotal = {}
    allGuardsTotal[0] = 0
    #allGuardsDays = {}
    for day in allDays:
        timeKeys = list(allDays[day].keys())
        print(day)
        print(timeKeys)
        if not len(timeKeys) == 0:
            length = len(timeKeys)
            number = allDays[day][timeKeys[0]].split(" ")[2][1:]
            
            if number not in allGuards:
                allGuards[number] = [0]*60
                allGuardsTotal[number] = 0
            for i in range(int((length-1)/2)):
                a = int(timeKeys[i*2+1].split(":")[1])
                b = int(timeKeys[i*2+2].split(":")[1])
                for x in range(a, b):
                    allGuards[number][x] += 1
                allGuardsTotal[number] += (b-a)
    
    print("---------")
    maxIndex = 0
    for guard in allGuards:
        print("Guard " + guard + ":" + str(allGuardsTotal[guard]))
        if allGuardsTotal[guard] > allGuardsTotal[maxIndex]:
            maxIndex = guard
    
    currentMaxMinutes = 0
    currentMaxGuard = 0
    currentMaxMinute = 0
    for guard in allGuards:
        for x in range(60):
            if allGuards[guard][x] > currentMaxMinutes:
                currentMaxGuard = int(guard)
                currentMaxMinutes = allGuards[guard][x]
                currentMaxMinute = x
    
    print("Guard Number: " + str(currentMaxGuard))
    print("Max Minute " + str(currentMaxMinute) + " mit " + str(currentMaxMinutes) + " Minuten")
    print("mult: " + str(currentMaxGuard*currentMaxMinute))


def stratEins():
    print("maxIndex: " + str(maxIndex))
    maxArray = allGuards[maxIndex]
    maxMinIndex = 0
    maxMins = 0
    for x in range(60):
        print(str(x) + ": " + str(maxArray[x]))
        if maxArray[x] > maxMins:
            maxMinIndex = x
            maxMins = maxArray[x]
    
    print("maxMinIndex " + str(maxMinIndex) + " mit " + str(maxMins) + " maxMins")
    print("Mult: " + str(int(maxIndex)*maxMinIndex))
        
            
        
        
        
    

if __name__== "__main__":
    doSomething()