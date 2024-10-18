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

import ctypes
rg = ctypes.CDLL('./src/runge-kutta/rk.dll')
rg.runge_kutta.argtypes = [ctypes.c_float, ctypes.POINTER(ctypes.c_float)]
rg.runge_kutta.restype = None
h = 0.04

def setup():
    global buffer,buffer2, p1, p2, center, wB1, plot, hB2
    size(width,height)
    buffer = create_graphics(width,wB1)
    buffer2 = create_graphics(width,hB2)
    buffer.clear()
    center = Vector(width/4, height/2)

    p1 = Pendulum(0,20,100,np.pi/6, buffer,center,[255,0,0])
    p2 = Pendulum(0,20,100,0,buffer, p1.drawPos,[0,0,255], p1)
    plot = Plot(buffer2,wB1)
    buffer.stroke(0,0,0,20)
    buffer.stroke_weight(1)
    

def draw():
    global buffer, buffer2
    background('#33E06A')
    push()
    translate(width/2,0)
    rotate(np.pi/2)
    p1.draw()
    p2.center = p1.drawPos
    p2.draw()
    p1.drawMass()
    p2.drawMass()
    con_iniciales = np.array([p1.v_angle, p2.v_angle,p1.position.angle, p2.position.angle], dtype=np.float32)
    rg.runge_kutta(h, con_iniciales.ctypes.data_as(ctypes.POINTER(ctypes.c_float)))
    p1.position.angle = con_iniciales[2]
    p2.position.angle = con_iniciales[3]
    p1.v_angle = con_iniciales[0]
    p2.v_angle = con_iniciales[1]
    image(buffer,0,0,width,wB1)
    pop()
    plot.draw([p1,p2])
    DrawAxes()
    image(buffer2,wB1,150,width,wB1)

    # print(f'{con_iniciales[0]}, {con_iniciales[1]},{con_iniciales[2]},{con_iniciales[3]}')
    
def DrawAxes():
    line([wB1, height/2],[width,height/2])
    line([wB1, 150],[wB1,350])
