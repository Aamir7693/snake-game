from turtle import Turtle
class GScore:
    def __init__(self):
        self.scor=0
        self.score=Turtle()
        self.score.showturtle()
        self.score.penup()
        self.score.goto(0,270)
        self.score.pendown()
        self.score.hideturtle()
        self.score.color("white")
        self.score.shape('classic')
        scorestring = ("Score: %s" % self.scor)
        self.score.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

    def update(self):
        self.scor+=1
        scorestring = ("Score: %s" % self.scor)
        self.score.clear()
        self.score.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
    def hit(self):
        self.score.penup()
        self.score.goto(-200,0)
        self.score.pendown()
        scorestring = ("Wall Hit Detected Game Over !!!")
        self.score.color("red")
        self.score.write(scorestring, False, align='left', font=('Arial', 20, 'normal'))
