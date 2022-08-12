import turtle

t=turtle.Turtle()
t.penup()
#set the position of turtle to draw the outline of Logo
t.goto(-20,-70)
#set the color
t.color("#F0DB4F","#F0DB4F")
t.begin_fill()
t.pendown()
t.left(165)
t.forward(100)
t.right(70)
t.forward(220)
t.setheading(0)
t.forward(229)

t.penup()

t.goto(-20,-70)
t.setheading(0)
t.pendown()
t.left(15)
t.forward(100)
t.left(70)
t.forward(229)
t.end_fill()
t.penup()

#set the position to draw 'J'
t.goto(-35,-20)
t.setheading(90)
t.color("white","white")
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(20)
t.left(90)
t.forward(130)
t.setheading(90)
t.left(75)
t.forward(40)
t.left(110)
t.forward(20)

t.penup()
t.goto(-35,-20)
t.setheading(90)
t.left(75)
t.pendown()
t.forward(60)
t.end_fill()
t.penup()

#Draw the yellow box for 's' letter
t.color("yellow","yellow")
#Set the position
t.goto(-20,-55)
t.setheading(90)
t.pendown()
t.begin_fill()
t.forward(215)
t.right(90)
t.forward(100)
t.right(95)
t.forward(195)
t.left(90)
t.end_fill()
t.penup()

#Draw the S of the Dell Logo
t.color("white","white")
t.pensize(2)
t.goto(-10,-20)
t.begin_fill()
t.setheading(0)
t.left(15)
t.pendown()
t.forward(65)
t.left(70)
t.forward(70)
t.left(90)
t.left(15)
t.forward(50)
t.right(100)
t.forward(50)
t.right(90)
t.forward(50)
t.left(85)
t.forward(20)
t.left(95)
t.forward(70)
t.left(90)
t.forward(90)
t.left(100)
t.forward(50)
t.right(105)
t.forward(37)
t.right(75)
t.forward(50)
t.left(85)
t.forward(20)
t.end_fill()

t.hideturtle()
turtle.done()
