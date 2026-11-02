# Nicolas Posso
# 11/01/2026
# P4LAB1A - Turtle House

import turtle

window = turtle.Screen()
window.title("P4LAB1A - My Turtle House")
window.bgcolor("lightblue")

house = turtle.Turtle()
house.shape("turtle")
house.speed(4)
house.pensize(3)
house.pencolor("darkgreen")

house.penup()
house.goto(-60, -80)
house.setheading(0)
house.pendown()

side = 0
while side < 4:
    house.forward(120)
    house.left(90)
    side = side + 1

house.penup()
house.goto(-60, 40)
house.setheading(0)
house.pendown()

house.fillcolor("forestgreen")
house.begin_fill()

for side in range(3):
    house.forward(120)
    house.left(120)

house.end_fill()

turtle.done()