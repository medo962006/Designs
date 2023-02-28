import turtle
colors=['red','yellow','green','blue','purple','orange']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
for x in range(100000000):
    t.pencolor(colors[x%6])
    t.width(x/100 +1)
    t.forward(x/100)
    t.left(59)
turtle.done()