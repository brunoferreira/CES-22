import turtle # Tess becomes a traffic light.
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")


wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0

def advance_state_machine():
    global state_num
    if state_num == 0: # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1: # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2

    else: # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0

def change_color_to_r():
    tess.color("red")

def change_color_to_g():
    tess.color("green")

def change_color_to_b():
    tess.color("blue")

def increase_width():
    w = tess.width() 
    if w < 20:
        tess.width(w+1) 

def decrease_width():
    w = tess.width()
    if w > 1:
        tess.width(w-1)

def move_up():
    tess.setheading(90)
    tess.forward(20)

def move_right():
    tess.setheading(0)
    tess.forward(20)

def move_down():
    tess.setheading(270)
    tess.forward(20)

def move_left():
    tess.setheading(180)
    tess.forward(20)

# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")
wn.onkey(change_color_to_r, "r")
wn.onkey(change_color_to_g, "g")
wn.onkey(change_color_to_b, "b")
wn.onkey(increase_width, "plus")
wn.onkey(decrease_width, "minus")
wn.onkey(move_up, "w")
wn.onkey(move_right, "d")
wn.onkey(move_down, "s")
wn.onkey(move_left, "a")

wn.listen() # Listen for events
wn.mainloop()
