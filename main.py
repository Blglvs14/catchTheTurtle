import turtle
import random

screen = turtle.Screen()
screen.bgcolor("beige")
screen.title("Catch The Turtle")
FONT = ('Times New Roman', 30, 'bold')
turtleList = []
score = 0
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
grid_size = 10
game_over = False

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setposition(0, y)
    score_turtle.write(arg="Puan: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        #print(x, y) click yaptığın koordinatları terminale yazar
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Puan: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtleList.append(t)

'''
make_turtle(-20,20)
make_turtle(-10,20)
make_turtle(0,20)
make_turtle(10,20)
make_turtle(20,20)

make_turtle(-20,10)
make_turtle(-10,10)
make_turtle(0,10)
make_turtle(10,10)
make_turtle(20,10)

make_turtle(-20,0)
make_turtle(-10,0)
make_turtle(0,0)
make_turtle(10,0)
make_turtle(20,0)

make_turtle(-20,-10)
make_turtle(-10,-10)
make_turtle(0,-10)
make_turtle(10,-10)
make_turtle(20,-10)
'''

def setup_turtle():
    for x in range(-20,30,10):
        for y in range(-20,20,10):
            make_turtle(x, y)
            turtle.hideturtle()

def hide_turtles():
    for t in turtleList:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

def countdown(time):
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    global game_over

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setposition(0, y-40)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Oyun Bitti!", move=False, align="center", font=FONT)

turtle.tracer(0)            #nesneyi takip etmeyi bırak
setup_score_turtle()
setup_turtle()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)            #nesneyi takip etmeyi başlat

turtle.mainloop()
