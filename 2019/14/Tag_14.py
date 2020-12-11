# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

testing = False
testNumber = 3

class element:
    
    def __init__(self, n, x):
        self.anzahl = int(x)
        self.name = n
        self.zutaten = []
        self.zutatenAnzahl = []
        self.distance = 0
        print("Neues Element namens " + n + " erstellt!")
    
    def getName(self):
        return self.name
    
    def setAnzahl(self, x):
        self.anzahl = int(x)
    
    def addZutat(self,v,x):
        self.zutaten.append(v)
        self.zutatenAnzahl.append(int(x))
        return "Zutat hinzugefügt, " + v.getName() + " zu " + self.name + "\n"
    
    def getZutaten(self):
        return self.zutaten
    
    def getAnzahl(self):
        return self.anzahl
    
    def getZutatenAnzahl(self):
        return self.zutatenAnzahl
    
    def getZutatenString(self):
        st = ""
        for z in self.zutaten:
            st += z.getName() + "|"
        return st
    
    def getAnzahlString(self):
        return str(self.anzahl)
    
    def getZutatenAnzahlString(self):
        return str(self.zutatenAnzahl)
    

def doSomething():
    
    alleElemente = {}
    o = element("ORE", 1)
    alleElemente["ORE"] = o
    global testing
    global testNumber
    name = "input.txt"
    if testing:
        if testNumber == 1:
            name = "inputTest.txt"
        elif testNumber == 2:
            name = "inputTest2.txt"
        else:
            name = "inputTest3.txt"
    
    with open(name) as fp:
        rezepte = fp.readlines()
    fout = open("output.txt", "w+")
    
    #print(rezepte)
    for r in rezepte:
        r = r.rstrip()
        print(r)
        x = r.split("=>")
        
        print(x[0])
        print(x[1])
        print()
        zutatenRein = x[0].strip().split(",")
        zutatRaus = x[1].strip()
        zR = zutatRaus.split(" ")
        if zR[1] not in alleElemente:
            e = element(zR[1].strip(), zR[0].strip())
            alleElemente[zR[1].strip()] = e
        else:
            e = alleElemente[zR[1].strip()]
            e.setAnzahl(zR[0].strip())
        for el in zutatenRein:
            el = el.strip()
            zRe = el.split(" ")
            zRe[0] = zRe[0].strip()
            zRe[1] = zRe[1].strip()
            if zRe[1] not in alleElemente:
                e1 = element(zRe[1], 0)
                alleElemente[zRe[1]] = e1
            e1 = alleElemente[zRe[1]]
            e.addZutat(e1, zRe[0])
    
    for x in alleElemente:
        e = alleElemente[x]
        print(str(e.getAnzahl()) + " " + str(e.getName()) + " => " + e.getZutatenString() + "/" + e.getZutatenAnzahlString())
    
    current = alleElemente["FUEL"]
    queue = []
    elementeAnzahl = {}
    for e in alleElemente:
        elementeAnzahl[e] = 0
    for i in range(len(current.getZutaten())):
        name = current.getZutaten()[i].getName()
        queue.append(name)
        elementeAnzahl[name] = current.getZutatenAnzahl()[i]
    
    print("Queue: ")
    print(queue)
    print("elementeAnzahl: ")
    print(elementeAnzahl)
        
    while len(queue) > 0:
        elementName = queue.pop()
        el = alleElemente[elementName]
        mult = 1
        while mult*el.getAnzahl() < elementeAnzahl[elementName]:
            mult += 1
        print(mult)
        for i in range(len(el.getZutaten())):
            name = el.getZutaten()[i].getName()
            if name != "ORE":
                if name not in queue:
                    queue.append(name)
                elementeAnzahl[name] += el.getZutatenAnzahl()[i]*mult
                elementeAnzahl[elementName] = 0
        
        print("Queue: ")
        print(queue)
        print("elementeAnzahl: ")
        print(elementeAnzahl)
    
    print("----------")
    
    for name in elementeAnzahl:
        if elementeAnzahl[name] != 0:
            queue.append(name)
    
    while len(queue) > 0:
        
        print("Queue: ")
        print(queue)
        print("elementeAnzahl: ")
        for x in elementeAnzahl:
            if elementeAnzahl[x] != 0:
                print(x + " --> " + str(elementeAnzahl[x]))
        
        elementName = queue.pop()
        el = alleElemente[elementName]
        mult = 1
        while mult*el.getAnzahl() < elementeAnzahl[elementName]:
            mult += 1
        print("Mult für " + elementName + ": " + str(mult))
        for i in range(len(el.getZutaten())):
            name = el.getZutaten()[i].getName()
            elementeAnzahl[name] += el.getZutatenAnzahl()[i]*mult
            elementeAnzahl[elementName] = 0
        
    print("--------------------------------------------------")
    print("Final Queue: ")
    print(queue)
    print("Final elementeAnzahl: ")
    print(elementeAnzahl)
    print("--------------------------------------------------")
    print("Finale Anzahl an ORE: " + str(elementeAnzahl["ORE"]))
    
        
        

if __name__== "__main__":
    doSomething()