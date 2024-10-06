from p5 import *
from .pendulum import Pendulum
from .plot import Plot
width = 1000
height= 500
buffer = None
buffer2 = None

wB1 = int(width/2)
hB2 = int(height-300)

center = None
p1 = None
p2 = None
plot = None
def setup():
    global buffer,buffer2, p1, p2, center, wB1, plot, hB2
    size(width,height)
    buffer = create_graphics(width,wB1)
    buffer2 = create_graphics(width,hB2)
    buffer.clear()
    center = Vector(width/4, height/2)

    p1 = Pendulum(0,20,100,radians(360), buffer,center,[255,0,0])
    p2 = Pendulum(0,20,100,radians(360),buffer, p1.drawPos,[0,0,255], p1)
    plot = Plot(buffer2,wB1)

    buffer.stroke(0,0,0,20)
    buffer.stroke_weight(1)

def draw():
    global buffer, buffer2
    background('#33E06A')
    p1.draw()
    p2.center = p1.drawPos
    p2.draw()
    p1.drawMass()
    p2.drawMass()
    plot.draw([p1,p2])
    image(buffer,0,0,width,wB1)
    image(buffer2,wB1,150,width,wB1)
