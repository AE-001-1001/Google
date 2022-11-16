import numpy as np
import os 
import time as t
# Thank you for reading my code
# I hope you enjoyed it
# and Thank you universe for watching over my fallen brothers and sisters
# with love, ~A
class Human(object):
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def __str__(HumanArray):
        for a in HumanArray:
            print(f" {a.name} | {a.last_name} | {a.age} ".format(a))
        return HumanArray


class RandomAge(object):
    def __init__(self,age):
        self.age = age
    def agerandom(age):
        
        return np.random.randint(0,27, size=9)
# 27 club members list the first 10
Humans = np.array([Human("Alexandre", "Levy", 27.068),Human("Jim", "Morrison", 27.207), Human("Jimi", "Hendrix", 27.295), 
                   Human("Janis", "Joplin", 27.258), Human("Kurt", "Cobain", 27.044), Human("Amy", "Winehouse", 27.312), 
                   Human("Brian", "Jones", 27.125), Human("Alan", "Wilson", 27.061), Human("Jarad Anthony", "Higgins", 21.006)])

Humans_age = np.array([a.name for a in Humans if a.age > 27.1 or a.age < 21.0])

# initialize the array

def PreRunner():
    t.sleep(0.250)
    os.system("cls")
    Human.__str__(Humans)
    for a in Humans_age:
        print(len(a) * ".")
    for a in Humans:
        s = 0 
        s += a.age
        print(f"Trying to contact {a.name} {a.last_name}...")
        print(f"Random age: {RandomAge.agerandom(a)}")
    
    print(Humans_age)
    print("Ran successfully")
    return 0

def main():
    PreRunner()
    return 0

if __name__ == "__main__":
    # print how long it took to run the script
    start = t.time()
    for I in range(0, 2004):
        main()
    end = t.time()
    print(f"Time elapsed: {end - start}")
