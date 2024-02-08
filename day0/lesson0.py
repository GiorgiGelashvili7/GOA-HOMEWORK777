from turtle import *

#we want to paint a house

#step 1: draw a square
speed(2)
speed(3)
width(7)
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(200)

left(90)

#end of square
#drawing a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)

right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#drawing a window 

color("purple")
left(30)
forward(66)
color("brown")
left(90)
forward(66)
left(90)
forward(66)
left(90)
forward(66)
right(180)
forward(66)
right(90)
forward(33)
right(90)
forward(66)
right(180)
forward(33)
left(90)
forward(33)
right(180)
forward(66)
left(90)
forward(33)
left(90)
forward(66)
right(90)
forward(68)
right(90)
forward(66)
left(90)
forward(66)
left(180)
forward(66)
right(90)
forward(33)
right(90)
forward(33)
left(90)
forward(33)
right(180)
forward(66)
left(180)
forward(33)
right(90)
forward(33)
left(180)
forward(66)
right(90)
forward(33)
right(90)
forward(66)


exitonclick()