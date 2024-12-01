#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def adopted(self, owner_name):
        self.owner = owner_name        
        pass