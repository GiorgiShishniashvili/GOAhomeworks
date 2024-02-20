from turtle import *

speed(5)
width(7)

color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#doordrawing


forward(70)
color("yellow")

begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#roofdrawing

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#windowsdrawing

penup()
goto(50, 120)
pendown()

color("blue")
begin_fill()
right(60)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

#window_2

penup()
goto(150, 120)
pendown()

right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()






exitonclick()