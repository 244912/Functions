import turtle

okno = turtle.Screen()
okno.bgcolor("lightgreen")

zolw = turtle.Turtle()
zolw.speed(5)

bok = 100

for i in range(4):
    zolw.forward(bok)
    zolw.right(90)


zolw.hideturtle()
okno.mainloop()