from turtle import *
import random
shape("turtle")
speed(0)
colorList=["green", "yellow", "blue","red","orange","purple"]
def tree(size,levels,angle,colour):
    if levels==0:
        dot(size)
        color('green')
        return
    if levels%2==0:
        color(colorList[colour])
    forward(size)
    right(angle)
    tree(size*0.8,levels-1,angle,colour=random.randint(0,5))
    left(angle*2)
    tree(size*0.8,levels-1,angle,colour=random.randint(0,5))
    right(angle)
    backward(size)
left(90)
tree(70,5,45,0)
mainloop()