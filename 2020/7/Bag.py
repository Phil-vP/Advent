# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:27:59 2020

@author: perpphil
"""

class Bag:
    
    def __init__(self, name):
        self.name = name
        print("Bag " + name + " created")
        self.nachfolger = {}
        self.nachfolgerBags = {}
    
    def setNachfolger(self, name, number):
        self.nachfolger[name] = number
    
    def setNachfolgerMap(self, nachfolger_map):
        self.nachfolger = nachfolger_map
    
    def calcNachfolgerToBag(self, allBags):
        for name in list(self.nachfolger.keys()):
            self.nachfolgerBags[name] = allBags[name]
    
    def getNachfolger(self):
        return self.nachfolger
    
    def getNumber(self):
        number = 1
        nameList = list(self.nachfolger.keys())
        for b in nameList:
            number += self.nachfolger[b] * self.nachfolgerBags[b].getNumber()
        
        return number