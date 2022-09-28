import re
class Person(object):
    def __init__(self, fname,lname):
        self.name = fname
        self.lname = lname
    def create_person(fname,lname):
        person = (fname +' '+ lname)
        return person
    def create_id(abc,id):
        dict = [("Got Person : "+ abc),("Got ID : %s" % id)]
        print('',dict[0],'\n',dict[1])
        return dict

a = Person.create_person('John','Marston')
b = Person.create_id(a,0)
fname = a
c = re.search("\s",a,1)
d = re.sub("\s"," ",a)
print(c,d)