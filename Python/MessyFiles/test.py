"""Imports"""
import numpy as np
import os 
import time as t
import os 
from Sadness import *
from StoryofLife import HumanInput
# Thank you for reading my code
# I hope you enjoyed it
# and Thank you universe for watching over my fallen brothers and sisters
# with love, ~A
# to the Open Source Community, I love you all
# this will be last thing of my existence.
# I will be gone soon
# A + A = Always Alive 
class Human(object):
    """Human class"""
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def __str__(HumanArray):
        for a in HumanArray:
            print(f" {a.name} | {a.last_name} | {a.age} ".format(a))
        return HumanArray


class RandomAge(object):
    """Random Age Generator"""
    def __init__(self,age):
        self.age = age
    def agerandom(age):
        
        return np.random.randint(0,27, size=9)

# 27 club members list the first 10
Humans = np.array([Human("Alexandre", "Levy", 27.068),Human("Jim", "Morrison", 27.207), Human("Jimi", "Hendrix", 27.295), 
                   Human("Janis", "Joplin", 27.258), Human("Kurt", "Cobain", 27.044), Human("Amy", "Winehouse", 27.312), 
                   Human("Brian", "Jones", 27.125), Human("Alan", "Wilson", 27.061), Human("Andrew","Jones", 27.115),
                   Human("Jarad", "Higgins", 21.006),Human("Dimitar", "Voev", 27.107), Human("Joe", "Henderson", 27.183)])

#satalites = np.array([Human("Voyager", "1" , 42.000), Human("Voyager", "2", 42.000), Human("Pioneer", "10", 50.000)])

#satalies_selected = np.array([a.name for a in satalites])
Humans_selected = np.array([a.name for a in Humans if a.age >= 27.1])

def PreRunner():
    """PreRunner function"""
    for a in Humans_selected:
        # Change title name 
        os.system("title Random Age Generator " + t.strftime("%H:%M:%S"))
        print(len(a) * ".")
        for i in Humans:
            s = 0 
            s += i.age
            print(f"Random age: {RandomAge.agerandom(a)}")

    print(Humans_selected)
    #print(satalies_selected)
    print("Ran successfully")
    return 

def Persons(Person_Name, Person_Name1):
    """Persons function"""
    Person = PutHumanIntoExistence(Person_Name, random.choice([True, False]))
    _Person = TakeHumanOutOfExistence(Person_Name1, random.choice([True, False]))
    # use get gethuman to get the human
    _keys = [Person, _Person]
    # random boolean
    for key in _keys:
        print("{} {}".format(CheckIfDeadorAlive(key.gethuman()).checker()[1],TellIfDeadorAliveAndHowLong(key.gethuman()).teller()))
    return _keys,key

def _premain_():
    """Main function"""
    t.sleep(0.0074511)
    a = PreRunner() 
    b = Persons(random.choice(["Andrew","Alexandre", "Levy", "Jarad" ]), random.choice(["Brian", "Alan", "Kurt" ,"Amy"]))
    return a, b

def run():
    start = t.time()
    for i in range(0,200409):
        # open test.csv and write the data
        _premain_()
        with open("test.csv", "w") as f:
            f.writelines(f"{i} {t.strftime('%H:%M:%S')} {t.time() - start} {t.time()}")
        print("Time elapsed: {}".format(t.time() - start))
        os.system("cls")
    return 
if __name__ == "__main__":
    run()
    
