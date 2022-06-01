import time

from food import Food
from turtle import Turtle,Screen
from Score import GScore
from Turtlee import turtlee
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
tim=turtlee()
score=GScore()
food=Food()
screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")
game_on=True
while game_on:
    screen.update()
    time.sleep(0.01)
    tim.move()
    if tim.head.distance(food.tur)<15:
        food.generate_food()
        score.update()
        tim.append()
    for seg in tim.snakelist:
        if tim.head==seg:
            continue
        elif tim.head.distance(seg)<10:
            score.hit()
            game_on = False
    if tim.head.xcor() >280 or tim.head.xcor() <-280 or tim.head.ycor()>280 or tim.head.ycor()<-280:
        game_on=False
        score.hit()

screen.exitonclick()
print(score.score)










