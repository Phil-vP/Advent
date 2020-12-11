# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

class planet:
    
    def __init__(self, n):
        self.name = n
        self.vorgaenger = []
        self.nachfolger = []
        self.marked = False
        self.distance = 0
        print("Neuer Planet namens " + n + " erstellt!")
    
    def getName(self):
        return "Name: " + self.name
    
    def addNachfolger(self, n):
        self.nachfolger.append(n)
        return "Nachfolger hinzugefügt, " + n.getName() + " zu " + self.name + str(self) + "\n"
        
    def addVorgaenger(self,v):
        self.vorgaenger.append(v)
        return "Vorgänger hinzugefügt, " + v.getName() + " zu " + self.name + str(self) + "\n"
    
    def getNachfolger(self):
        return self.nachfolger
    
    def getVorgaenger(self):
        return self.vorgaenger
    
    def countDirect(self):
        return len(self.vorgaenger)
    
    def countIndirect(self):
        counter = 0
        for v in self.vorgaenger:
            counter += v.countIndirect()
            #print("In planet " + self.name + ", counted " + v.getName())
        return len(self.vorgaenger) + counter
    
    def mark(self):
        self.marked = True
    

def doSomething():
    
    allPlanets = {}
    
    with open("input.txt") as fp:
        orbits = fp.readlines()
        
    fout = open("output.txt", "w+")
    
    #print(lines)
    for o in orbits:
        o = o.rstrip()
        print(o)
        p = o.split(")")
        first = str(p[0])
        second = str(p[1])
        
        if first in allPlanets:
            firstPlanet = allPlanets.get(first)
        else:
            fout.write("Planet " + first + " erstellt\n")
            firstPlanet = planet(first)
            allPlanets[first] = firstPlanet
        
        if second in allPlanets:
            secondPlanet = allPlanets.get(second)
        else:
            fout.write("Planet " + second + " erstellt\n")
            secondPlanet = planet(second)
            allPlanets[second] = secondPlanet
        
        fout.write(firstPlanet.addNachfolger(secondPlanet))
        #fout.write(first + " added Nachfolger " + second + "\n")
        fout.write(secondPlanet.addVorgaenger(firstPlanet))
        #fout.write(second + " added Vorgänger " + first + "\n")
        
        
    
        for p in allPlanets:
            fout.write(allPlanets.get(p).getName() + "\n")
            n = allPlanets.get(p).getNachfolger()
            fout.write("Nachfolger:\n")
            for x in n:
                fout.write("   N-" + x.getName() + "\n")
            v = allPlanets.get(p).getVorgaenger()
            fout.write("Vorgänger:\n")
            for x in v:
                fout.write("   V-" + x.getName() + "\n")
            #fout.write(str(allPlanets.get(p)) + "\n")
            fout.write("---\n")
        fout.write("----------------------------------------\n")
    fout.close()
    
    # Berechnen
    #counter = 0
    #for p in allPlanets:
        #indirect = allPlanets.get(p).countIndirect()-allPlanets.get(p).countDirect()
        #direct = allPlanets.get(p).countDirect()
        #counter += indirect + direct
        #print("Planet " + p + " hat " + str(indirect) + " indirekte und " + str(direct) + " direkte Orbits")
    #print("counter: " + str(counter))
    
    # Weg berechnen
    steps = 0
    queue = ["YOU"]
    
    while not "SAN" in queue:
        newqueue = []
        for p in queue:
            v = allPlanets.get(p).getVorgaenger()
            n = allPlanets.get(p).getNachfolger()
            
            for x in v:
                if x not in queue and x.marked == False:
                    newqueue.append(x.name)
            for x in n:
                if x not in queue and x.marked == False:
                    newqueue.append(x.name)
        
            allPlanets.get(p).mark()
        steps += 1
        queue = newqueue
        
    print(str(steps-2) + " Steps")

if __name__== "__main__":
    #print(getFull("01"))
    #test()
    doSomething()