# Nicolas Posso
# 11/01/2026
# P4LAB1B - Initials

import turtle

window = turtle.Screen()
window.title("P4LAB1B - My Initials")
window.bgcolor("lightblue")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(4)
pen.pensize(8)
pen.pencolor("darkgreen")

pen.penup()
pen.goto(-120, -80)
pen.setheading(90)
pen.pendown()

pen.forward(140)
pen.right(150)
pen.forward(161)
pen.setheading(90)
pen.forward(140)

pen.penup()
pen.goto(40, -80)
pen.setheading(90)
pen.pendown()

pen.forward(140)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(70)
pen.right(90)
pen.forward(70)

turtle.done()