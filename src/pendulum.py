from p5 import Vector, circle,fill, line, stroke,radians, no_stroke
import numpy as np
class Pendulum:
    def __init__(self, mass: float , l:float, angle:float, buffer, center, pendulum:'Pendulum' = None) -> None:
        self.mass = mass
        self.buffer = buffer
        self.long = l
        self.angle = angle
        self.center = center
        self.pendulum = pendulum 
        self.position = Vector(np.sin(angle)*self.long, np.cos(angle)*self.long) 
        self.drawPos = self.position + self.center
        self.posBefore = None
    
    def draw(self):
        self.drawPos = self.position + self.center
        self.position.rotate(radians(self.angle))
        line(self.center, self.drawPos)

    def drawMass(self):
        no_stroke()
        circle(self.drawPos.x,self.drawPos.y,self.mass)
        if self.pendulum != None:
            if self.posBefore != None:
                self.buffer.line(self.posBefore,self.drawPos)
            self.posBefore = self.drawPos
        stroke(0)
  
