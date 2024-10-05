from p5 import *
from .pendulum import Pendulum
width = 800
height= 600
buffer = None

center = None
p1 = None
p2 = None
def setup():
    global buffer, p1, p2,p3, center
    size(width,height)
    buffer = create_graphics(width,height)
    buffer.clear()
    center = Vector(width/2, height/2)
    p1 = Pendulum(20,100,radians(-200), buffer,center)
    p2 = Pendulum(20,100,radians(180),buffer, p1.drawPos, p1)
    buffer.stroke(50)
    fill(255,0,0)
    stroke(0)    

def draw():
    global buffer
    background('#33E06A')
    p1.draw()
    p2.center = p1.drawPos
    p2.draw()
    p1.drawMass()
    p2.drawMass()
    image(buffer,0,0)
