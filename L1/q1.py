import turtle

def draw_squares(t, size, increment, n):
    """ 
        Draw {n} squares with sizes starting at {size} and incrementing
        {increment} at each iteration
    """
    t.width(5)
    t.color((208/255, 108/255, 170/255))
    
    for i in range(n):
        draw_centralized_square(t, size + i * increment)
    
    t.penup()
    t.setpos((- (size + n * increment) / 2, - (size + n * increment) / 2))
    t.pendown()
    t.setheading(0)


def draw_centralized_square(t, size):
    """ Draw a centralized square with size {size}
    """
    t.penup()
    t.setpos((-size/2, -size/2))
    t.pendown()
    
    t.setheading(0)
    for i in range(4):
        t.forward(size)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Question 1")
jackie = turtle.Turtle()
draw_squares(jackie, 20, 20, 5)
wn.mainloop()