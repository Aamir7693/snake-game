
from turtle import Turtle
import random
class Food:
    def __init__(self):
       self.create_food()
       self.generate_food()


    def create_food(self):
        self.tur = Turtle()
        self.tur.turtlesize(0.5)
        self.tur.color("green")
        self.tur.shape("circle")
        self.tur.penup()
        self.tur.speed("fastest")

    def generate_food(self):
        x=random.randint(-280, 280)
        y=random.randint(-280, 280)
        self.tur.goto(x,y)