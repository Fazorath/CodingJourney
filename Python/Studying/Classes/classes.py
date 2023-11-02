class Dog:  # Define a class called dog / Capital represents a class
    '''A simple attempt at modeling a dog'''

    def __init__(self, name, age):
        '''Initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate the dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!")
