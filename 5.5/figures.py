import turtle

def draw_square(bok):
    for i in range(4):
        turtle.forward(bok)
        turtle.right(90)

def draw_triangle(bok):
    # Trójkąt równoboczny (wszystkie boki równe)
    for i in range(3):
        turtle.forward(bok)
        turtle.left(120)

def draw_rectangle(a, b):
    for i in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)