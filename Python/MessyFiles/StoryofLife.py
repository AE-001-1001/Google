import random as r
import numpy as np

class InputReader(object):
    def __init__(self, input, feeling):
        self.input = input
        self.feeling = feeling

    def inputReader(input):
        return input
    
    def feelingReader(feeling):
        return feeling

class Human(object):
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.name} | {self.last_name} | {self.age}"

# Combine the two classes
class HumanInput(InputReader, Human):
    def __init__(self, name, last_name, age, input, feeling):
        Human.__init__(self, name, last_name, age)
        InputReader.__init__(self, input, feeling)

    def __str__(self):
        return f"{self.name} | {self.last_name} | Age: {self.age} | Input: {self.input} | Feeling: {self.feeling}"
    

# use HumanInput to create a new human
Person = HumanInput("Andrew", "Jones", 18.144, "Hello", "Sad")
print(Person)
    