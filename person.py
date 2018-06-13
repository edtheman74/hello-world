#!/usr/bin/python3.6

class Person:
    def __init__(self, name):
        self.name = name;
    def say_hi_to(self, person):
        return f"Hi {person.name}, it's me, {self.name}."

ed = Person("Ed")
nathan = Person("Nathan")

print(ed.say_hi_to(nathan))
