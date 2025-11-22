import figures
import turtle

# Ustawiamy okno
okno = turtle.Screen()
okno.bgcolor("lightgreen")

# Tworzymy żółwia
zolw = turtle.Turtle()
zolw.speed(5)

# 1. Dwa kwadraty
zolw.penup()
zolw.goto(-180, 120)
zolw.pendown()
figures.draw_square(70)

zolw.penup()
zolw.goto(80, 120)
zolw.pendown()
figures.draw_square(70)

# 2. Dwa trójkąty
zolw.penup()
zolw.goto(-180, 0)
zolw.pendown()
figures.draw_triangle(90)

zolw.penup()
zolw.goto(80, 0)
zolw.pendown()
figures.draw_triangle(90)

# 3. Dwa prostokąty
zolw.penup()
zolw.goto(-180, -120)
zolw.pendown()
figures.draw_rectangle(100, 50)

zolw.penup()
zolw.goto(80, -120)
zolw.pendown()
figures.draw_rectangle(100, 50)

# Kończymy
zolw.hideturtle()
okno.mainloop()