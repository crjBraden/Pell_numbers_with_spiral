import turtle
s = turtle.Screen()
t = turtle.Turtle()

first = 0
sec = 1

for i in range(13):
    n = first
    first = sec
    sec = 2*sec + n
    t.forward(1)
    t.circle(sec, 90)
    print(sec)
