import random


class userinput(object):
    def __init__(self, intention, feeling):
        self.intention = intention
        self.feel = feeling
    def conjugate(intention,feeling):
        a = [intention,feeling]
        return a[0],a[1]

class UserReader(userinput):
    def __init__(self, intention, feeling):
        self.intention = intention
        self.feel = feeling
    def CheckReader(intention,feeling):
        a = intention
        b = feeling
        return a,b
    def PrintReader(a,b):
        responses = ['Ur Mum likes goatss','You were sent here to die','You were sent here to change the world']
        if a == 'Good':
            print("I am glad your intention is good.")
            pass
        if a == 'Bad':
            print("I am sorry for yourself.")
            pass
        if a == 'Unknown':
            print("If your intention is unknown, please reconsider your intentions.")
            pass
        if b == 'Good':
            print("I am glad your feeling is good.")
            pass
        if b == 'Sadness':
            print("It is okay to be sad, but don't let it consume you from the inside out.")
        if b == 'Sad':
            print(random.choices(responses))
            pass
        return a,b



a = userinput.conjugate('Good','Sad')
print(UserReader.CheckReader(a[0],a[1]))

