# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""
import math
import itertools
import time

testing = False
numberTest = 2

class moon:
    def __init__(self, name, p1, p2, p3):
        self.name = name
        self.pos = [p1,p2,p3]
        self.vel = [0,0,0]
    
    def setPos(self, p1, p2, p3):
        self.pos[0] = p1
        self.pos[1] = p2
        self.pos[2] = p3
    def setVel(self, v1, v2, v3):
        self.vel[0] = v1
        self.vel[1] = v2
        self.vel[2] = v3
    def getPos(self):
        return self.pos
    def getVel(self):
        return self.vel
    def getName(self):
        return self.name
    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[2] += self.vel[2]
    def getPot(self):
        return abs(self.pos[0])+abs(self.pos[1])+abs(self.pos[2])
    def getKin(self):
        return abs(self.vel[0])+abs(self.vel[1])+abs(self.vel[2])

def moons():
    global testing
    global numberTest
    allMoons = []
    m1 = moon("Io", -10,-13,7)
    allMoons.append(m1)
    m2 = moon("Europa", 1,2,1)
    allMoons.append(m2)
    m3 = moon("Ganymede", -15,-3,13)
    allMoons.append(m3)
    m4 = moon("Io", 3,7,-4)
    allMoons.append(m4)
    if testing:
        if numberTest == 1:
            allMoons[0].setPos(-1,0,2)
            allMoons[1].setPos(2,-10,-7)
            allMoons[2].setPos(4,-8,8)
            allMoons[3].setPos(3,5,-1)
        else:
            allMoons[0].setPos(-8,-10,0)
            allMoons[1].setPos(5,5,10)
            allMoons[2].setPos(2,-7,3)
            allMoons[3].setPos(9,-8,-3)
    print("Nach 0 steps:")
    steps = 10
    printMoons(allMoons)
    allCons = []
    allConsFirst = []
    counter = 1
    start = time.time()
    firstState = ""
    for m in allMoons:
        for p in m.getPos():
            firstState += str(p) + "|"
        for v in m.getVel():
            firstState += "|" + str(v)
        firstState += "§"
    #for i in range(steps):
    while True:
        liste = list(itertools.combinations('0123',2))
        for l in liste:
            setVelocity(allMoons[int(l[0])], allMoons[int(l[1])])
        
        for m in allMoons:
            p = m.getPos()
            v = m.getVel()
            for p in m.getPos():
                state += str(p) + "|"
            for v in m.getVel():
                state += "|" + str(v)
            state += "§"
        if state == firstState:
            print("Nach " + str(counter) + " steps gefunden!")
            print(state)
            
            print("Nach " + str(counter) + " steps:")
            printMoons(allMoons)
            break
        #elif counter > 2800:
            #break
        else:
            counter += 1
            if counter%100000 == 0:
                now = time.time()
                print(str(counter) + ", " + str(now-start) + " seconds")
                start = now
            allCons.append(state)
            allConsFirst.append(state[:5])
        
        for m in allMoons:
            m.move()
        #if abs(counter-2772) < 5:
        #if (i+1)%(steps/10) == 0:
            #print("Nach " + str(counter) + " steps:")
            #printMoons(allMoons)
        
    print()
    print("Energy after " + str(counter) + " Steps:")
    getEnergy(allMoons)

def moonsTwo():
    global testing
    global numberTest
    allMoons = []
    m1 = moon("Io", -10,-13,7)
    allMoons.append(m1)
    m2 = moon("Europa", 1,2,1)
    allMoons.append(m2)
    m3 = moon("Ganymede", -15,-3,13)
    allMoons.append(m3)
    m4 = moon("Io", 3,7,-4)
    allMoons.append(m4)
    if testing:
        if numberTest == 1:
            allMoons[0].setPos(-1,0,2)
            allMoons[1].setPos(2,-10,-7)
            allMoons[2].setPos(4,-8,8)
            allMoons[3].setPos(3,5,-1)
        else:
            allMoons[0].setPos(-8,-10,0)
            allMoons[1].setPos(5,5,10)
            allMoons[2].setPos(2,-7,3)
            allMoons[3].setPos(9,-8,-3)
    print("Nach 0 steps:")
    printMoons(allMoons)
    counter = 1
    start = time.time()
    xStart = ""
    yStart = ""
    zStart = ""
    xFound = False
    yFound = False
    zFound = False
    xSteps = 0
    ySteps = 0
    zSteps = 0
    for m in allMoons:
        p = m.getPos()
        v = m.getVel()
        xStart += str(p[0]) + "|" + str(v[0])
        yStart += str(p[1]) + "|" + str(v[1])
        zStart += str(p[2]) + "|" + str(v[2])
            
    while True:
        liste = list(itertools.combinations('0123',2))
        for l in liste:
            setVelocity(allMoons[int(l[0])], allMoons[int(l[1])])
        
            
        xState = ""
        yState = ""
        zState = ""
        for m in allMoons:
            p = m.getPos()
            v = m.getVel()
            xState += str(p[0]) + "|" + str(v[0])
            yState += str(p[1]) + "|" + str(v[1])
            zState += str(p[2]) + "|" + str(v[2])
            
        if not xFound and xState == xStart:
            print("X nach " + str(counter) + " steps gefunden!")
            xSteps = counter
            print(xState)
            xFound = True
        if not yFound and yState == yStart:
            print("Y nach " + str(counter) + " steps gefunden!")
            ySteps = counter
            print(yState)
            yFound = True
        if not zFound and zState == zStart:
            print("Z nach " + str(counter) + " steps gefunden!")
            zSteps = counter
            print(zState)
            zFound = True
        #elif counter > 2800:
            #break
        if xFound and yFound and zFound:
            print("xSteps: " + str(xSteps) + ", ySteps: " + str(ySteps) + ", zSteps: " + str(zSteps))
            lcm1 = int((xSteps*ySteps)/math.gcd(xSteps,ySteps))
            print("lcm1: " + str(lcm1))
            lcm = (lcm1*zSteps)/math.gcd(lcm1,zSteps)
            print("lcm: " + str(lcm))
            break
        else:
            counter += 1
            if counter%100000 == 0:
                now = time.time()
                print(str(counter) + ", " + str(now-start) + " seconds")
                start = now
        
        for m in allMoons:
            m.move()
        #if abs(counter-2772) < 5:
        #if (i+1)%(steps/10) == 0:
            #print("Nach " + str(counter) + " steps:")
            #printMoons(allMoons)
        
    print()
    print("Energy after " + str(counter) + " Steps:")
    getEnergy(allMoons)

def getEnergy(moons):
    energy = []
    alleZusammen = 0
    for m in moons:
        total = m.getPot()*m.getKin()
        print("pot: " + str(m.getPot()) + ", kin: " + str(m.getKin()) + ", total: " + str(total))
        energy.append(total)
        alleZusammen += total
    print("Sum of total energy: " + str(energy[0]) + " + " + str(energy[1]) + " + " + str(energy[2]) + " + " + str(energy[3]) + " = " + str(alleZusammen))
    
def setVelocity(m1,m2):
    pos1 = m1.getPos()
    vel1 = m1.getVel()
    pos2 = m2.getPos()
    vel2 = m2.getVel()
    #print()
    #print("----Moon 1: " + m1.getName() + ", Moon2: " + m2.getName() + "----")
    for i in range(3):
        x = pos1[i]-pos2[i]
        #print("i: " + str(i))
        #print("Pos1: " + str(pos1[i]) + ", Pos2: " + str(pos2[i]))
        if int(x) is not 0:
            x /= abs(x)
            #print("x: " + str(x))
            #print("oldVel1: " + str(vel1[i]) + ", oldVel2: " + str(vel2[i]))
            vel1[i] -= int(x)
            vel2[i] += int(x)
            #print("newVel1: " + str(vel1[i]) + ", newVel2: " + str(vel2[i]))

def printMoons(moons):
    for x in moons:
        print("Pos:" + str(x.getPos()) + ", Vel: " + str(x.getVel()))
    print()

if __name__== "__main__":
    #f = open("output.txt", "w+")
    #f.write("")
    #f.close()
    start = time.time()
    moonsTwo()
    dur = time.time() - start
    print("Duration: " + str(dur) + " seconds")