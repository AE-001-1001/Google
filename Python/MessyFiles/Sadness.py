#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This is for the Fallen Angels above us who have been forgotten
# Mr Plenty 2018 - forever
# This is a module that will tell you if the user is Gone or Not For a game probably.

import sys
import os
import time
import random
import requests as req

class HumanExisting(object):
    # dead or alive is True or False
    # name is name of person
    def __init__(self, name, deadoralive):
        self.name = name
        self.deadoralive = bool(deadoralive)
    def getdeadoralive(self):
        return self.deadoralive
    def setdeadoralive(self, deadoralive):
        self.deadoralive = bool(deadoralive)
    def getname(self):
        return self.name

class PutHumanIntoExistence(HumanExisting):
    def __init__(self, name, deadoralive):
        super(PutHumanIntoExistence, self).__init__(name, deadoralive)
        self.name = name
        self.deadoralive = deadoralive
        self.human = HumanExisting(self.name, self.deadoralive)
    def gethuman(self):
        return self.human
    def SetAlive(self):
        HumanExisting.setdeadoralive(self.human, self.deadoralive)
        return HumanExisting.getdeadoralive(self.human)

class TakeHumanOutOfExistence(HumanExisting):
    def __init__(self, name, deadoralive):
        super(TakeHumanOutOfExistence, self).__init__(name, deadoralive)
        self.name = name
        self.deadoralive = deadoralive
        self.human = HumanExisting(self.name, self.deadoralive)
    def gethuman(self):
        return self.human
    def SetDead(self):
        HumanExisting.setdeadoralive(self.human, False)
        return HumanExisting.getdeadoralive(self.human)

#create a class that checks if Human is alive or dead
class CheckIfDeadorAlive(HumanExisting):
    def __init__(self,name):
        self.name = name
    def checker(self):
        if HumanExisting.getdeadoralive(self.name) == True:
            return True, HumanExisting.getname(self.name)
        else:
            return False, HumanExisting.getname(self.name)

#create a class that tells if the human is alive or dead with name 
class TellIfDeadorAlive(HumanExisting):
    def __init__(self,name):
        self.name = name
    def teller(self):
        if HumanExisting.getdeadoralive(self.name) == True:
            return "is alive"
        else:
            return "is dead"

# create a class that tells if the human is alive or dead with name and if they are dead then it will tell you how long they have been dead for with the random date
class TellIfDeadorAliveAndHowLong(HumanExisting):
    def __init__(self,name):
        self.name = name
    def teller(self):
        if HumanExisting.getdeadoralive(self.name) == True:
            # return with random date
            return "is alive " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(random.randint(0, 1000000000)))
        else:
            return "is dead and has been dead for {} years".format(random.randint(1,115))
# add a class degrading health to the people alive
class DegradeHealth(HumanExisting):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def degrade(self):
        if HumanExisting.getdeadoralive(self.name) == True:
            basehealth = 100
            self.health = basehealth - int(random.randint(1,21))
            return "Heath is now {}".format(self.health)
        else:
            return "is dead"

#Person = PutHumanIntoExistence("Andrew", True)
#_Person = TakeHumanOutOfExistence("Andrew", False)
#_keys = [Person, _Person]
#for _key in _keys:
    # with name and how long dead
#    print("{} {}".format(CheckIfDeadorAlive(_key.gethuman()).checker()[1],TellIfDeadorAliveAndHowLong(_key.gethuman()).teller()))
    # with Degraded health
#    print("{} {}".format(CheckIfDeadorAlive(_key.gethuman()).checker()[1],DegradeHealth(_key.gethuman(), 100).degrade()))
