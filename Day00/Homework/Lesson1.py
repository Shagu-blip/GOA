from turtle import*
#we want to paint the house
#step 1: we want to draw a square
width(7)
color("orange")
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
#end of square
#drawing door
forward(70)
color("blue")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("orange")
left(30)
forward(20)
color("black")
color("skyblue")
begin_fill()
left(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()
left(180)
forward(51)
color("orange")
forward(129)
left(90)
forward(200)
left(90)
forward(200)
right(180)
forward(20)
color("skyblue")
begin_fill()
right(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()
exitonclick()