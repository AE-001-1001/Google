from random import random,choice,randint
from time import strftime
class Life(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(string):
        return string.name + " %s" % string.age
    
    def citizendatabase(string,age):
        dict = {age:string}
        return dict
    
    def getDatabase(XYz):
        dict = [XYz]
        return dict

class causeofdeath(object):
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cause(name):
        #Common causes of death from https://www.cdc.gov/nchs/fastats/leading-causes-of-death.htm
        CommonDeaths = {1:'Overdose', 2:'Disease', 3:'Suicide',
                   4:'Comatose', 5:'KIA', 6:'Heart Failure', 
                   7:'Heart Disease', 8:'Cancer', 9:'Alzheimers',
                   10:'Stroke',11:'Diabetes',12:'Influenza',
                   13:'Pneumonia',14:'Unintentional Injury',15:'Car Crash'
                    }
        print("Name of citizen: %s" % name)
        print("Cause of death: %s" % choice(CommonDeaths),"\nTime Citizen departed: %s "% {strftime("%Y-%m-%d %H:%M:%S")})
        return CommonDeaths

a = Life('Andrew', 18)
aa = Life.citizendatabase(a.name,a.age+randint(1,5))
aaa = causeofdeath.cause(a.name)
b = Life.getDatabase(aa)
print('Citizen Database:%s'%b)