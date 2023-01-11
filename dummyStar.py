from turtle import *

bgcolor('black')
width(0.01)
speed(100)
up()
goto(50,50)
down()

for i in range(1,75):
    if i%3==0:
        color('blue')
        bgcolor('red')
    elif i%3==1:
        color('green')
        bgcolor('blue')
    else:
        color('red')
        bgcolor('green')
    fd(300)
    rt(145)
