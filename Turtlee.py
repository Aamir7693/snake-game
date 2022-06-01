import time
from turtle import Turtle,Screen

class turtlee:
    def __init__(self):
        self.snakelist=[]
        self.create_snake()
        self.head=self.snakelist[0]

    def create_snake(self):
        listi=[0,-20,-40]
        for i in range(3):
            self.tim = Turtle()
            self.tim.penup()
            self.tim.shape("square")
            self.tim.color("white")
            self.tim.goto(0+listi[i], 0)
            self.snakelist.append(self.tim)
    def extend(self):
        position=self.snakelist[-1].position()
        return position
    def append(self):
        position=self.extend()

        self.tim = Turtle()
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.shape("square")
        self.tim.color("white")
        self.tim.speed("fastest")
        self.tim.goto(position)
        self.tim.showturtle()
        self.snakelist.append(self.tim)




    def move(self):
            for i in range(len(self.snakelist)-1,0,-1):
                x,y=self.snakelist[i-1].pos()
                self.snakelist[i].goto(x,y)
            self.snakelist[0].forward(20)
    def up(self):
        if self.snakelist[0].heading()==0:
            self.snakelist[0].left(90)
        elif self.snakelist[0].heading()==180:
            self.snakelist[0].right(90)
    def down(self):
        if self.snakelist[0].heading() == 0:
            self.snakelist[0].right(90)
        elif self.snakelist[0].heading() == 180:
            self.snakelist[0].left(90)
    def right(self):
        if self.snakelist[0].heading() == 0:
            self.snakelist[0].right(90)
        elif self.snakelist[0].heading() == 180:
            self.snakelist[0].right(90)
        elif self.snakelist[0].heading() == 90:
            self.snakelist[0].right(90)
        elif self.snakelist[0].heading() == 270:
            self.snakelist[0].left(90)
    def left(self):
        if self.snakelist[0].heading() == 0:
            self.snakelist[0].left(90)
        elif self.snakelist[0].heading() == 180:
            self.snakelist[0].left(90)
        elif self.snakelist[0].heading() == 90:
            self.snakelist[0].left(90)
        elif self.snakelist[0].heading() == 270:
            self.snakelist[0].right(90)






