import turtle

def draw_poly(t, n, sz):
    """ Draw a polygon with {n} sides and a side size equals to {sz}
    """
    t.width(5)
    t.color((208/255, 108/255, 170/255))
    
    angle = 360 / n

    for i in range(n):
        t.forward(sz)
        t.left(angle)
    t.setheading(0)
        

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Question 2")
jackie = turtle.Turtle()
draw_poly(jackie, 8, 50)
wn.mainloop()